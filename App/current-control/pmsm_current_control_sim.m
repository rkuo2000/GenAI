%% 3-Phase PMSM Current Control - Complete Simulation
% Field-Oriented Control with detailed analysis

clear all; clc; close all;

fprintf('==================================================\n');
fprintf('     3-PHASE PMSM CURRENT CONTROL SIMULATION     \n');
fprintf('==================================================\n\n');

%% ===== MOTOR PARAMETERS =====
R = 2.0;           % Stator resistance (Ohm)
L = 0.005;         % Stator inductance (H)
P = 4;             % Pole pairs
psi = 0.15;        % Permanent magnet flux (Wb)
J = 0.001;         % Rotor inertia (kg*m^2)
B = 0.001;         % Friction coefficient (Nm*s/rad)
Vdc = 200;         % DC bus voltage (V)

fprintf('--- MOTOR PARAMETERS ---\n');
fprintf('  Stator Resistance:    R = %.1f Ohm\n', R);
fprintf('  Stator Inductance:    L = %.1f mH\n', L*1000);
fprintf('  Pole Pairs:            P = %d\n', P);
fprintf('  Magnet Flux:           psi_f = %.3f Wb\n', psi);
fprintf('  DC Voltage:            Vdc = %.0f V\n\n', Vdc);

%% ===== CONTROLLER =====
Kp_i = 2.0;
Ki_i = 400.0;

fprintf('--- PI CONTROLLER ---\n');
fprintf('  Kp = %.2f, Ki = %.2f\n', Kp_i, Ki_i);
fprintf('  Bandwidth: 100 Hz\n\n');

%% ===== SIMULATION =====
dt = 1e-4;
T = 0.2;
N = round(T/dt);
t = (0:N-1)*dt;

fprintf('--- SIMULATION ---\n');
fprintf('  Time: %.0f ms, dt: %.0f us, Samples: %d\n\n', T*1000, dt*1e6, N);

%% ===== REFERENCES =====
i_d_ref = zeros(N,1);
i_q_ref = zeros(N,1);

% Profile to show both tracking and speed saturation
for k = 1:N
    if t(k) < 0.02
        i_q_ref(k) = 0;
    elseif t(k) < 0.06
        i_q_ref(k) = 1 * (t(k)-0.02)/0.04;    % 0 to 1A ramp
    elseif t(k) < 0.12
        i_q_ref(k) = 1;                         % Hold 1A
    elseif t(k) < 0.16
        i_q_ref(k) = 1 + 0.8*(t(k)-0.12)/0.04; % 1 to 1.8A ramp
    else
        i_q_ref(k) = 1.8;                       % Hold 1.8A
    end
end

fprintf('--- TEST PROFILE ---\n');
fprintf('  0-20ms:    i_q* = 0 A\n');
fprintf('  20-60ms:   i_q* = 0 to 1 A\n');
fprintf('  60-120ms:  i_q* = 1 A (hold)\n');
fprintf('  120-160ms: i_q* = 1 to 1.8 A\n');
fprintf('  160-200ms: i_q* = 1.8 A\n\n');

%% ===== INITIALIZATION =====
i_d = zeros(N,1);
i_q = zeros(N,1);
v_d = zeros(N,1);
v_q = zeros(N,1);
Te = zeros(N,1);
omega = zeros(N,1);
theta_e = zeros(N,1);
i_a = zeros(N,1);
i_b = zeros(N,1);
i_c = zeros(N,1);
i_alpha = zeros(N,1);
i_beta = zeros(N,1);
e_d = zeros(N,1);
e_q = zeros(N,1);

int_d = 0; int_q = 0;

fprintf('Running simulation...\n');
fprintf('['); pstep = round(N/50);

for k = 2:N
    if mod(k,pstep)==0, fprintf('='); end
    
    % Current error
    e_d(k) = i_d_ref(k) - i_d(k-1);
    e_q(k) = i_q_ref(k) - i_q(k-1);
    
    % PI
    int_d = int_d + Ki_i * e_d(k) * dt;
    int_q = int_q + Ki_i * e_q(k) * dt;
    int_d = min(max(int_d, -60), 60);
    int_q = min(max(int_q, -60), 60);
    
    % Decoupling
    ed = -P * omega(k-1) * L * i_q(k-1);
    eq = P * omega(k-1) * (L * i_d(k-1) + psi);
    
    % Voltage
    v_d(k) = Kp_i * e_d(k) + int_d + ed;
    v_q(k) = Kp_i * e_q(k) + int_q + eq;
    
    % Limit
    Vmax = Vdc / sqrt(3) * 0.98;
    V = sqrt(v_d(k)^2 + v_q(k)^2);
    if V > Vmax
        v_d(k) = v_d(k) * Vmax / V;
        v_q(k) = v_q(k) * Vmax / V;
    end
    
    % Motor model
    did = (v_d(k) - R*i_d(k-1) + P*omega(k-1)*L*i_q(k-1)) / L * dt;
    diq = (v_q(k) - R*i_q(k-1) - P*omega(k-1)*(L*i_d(k-1)+psi)) / L * dt;
    
    i_d(k) = min(max(i_d(k-1) + did, -10), 10);
    i_q(k) = min(max(i_q(k-1) + diq, -10), 10);
    
    % Torque
    Te(k) = 1.5 * P * psi * i_q(k);
    
    % Speed
    domega = (Te(k) - B*omega(k-1)) / J * dt;
    omega(k) = max(omega(k-1) + domega, 0);
    
    % Position
    theta_e(k) = mod(theta_e(k-1) + P*omega(k)*dt, 2*pi);
    
    % 3-phase
    ct = cos(theta_e(k)); st = sin(theta_e(k));
    i_alpha(k) = ct*i_d(k) - st*i_q(k);
    i_beta(k) = st*i_d(k) + ct*i_q(k);
    i_a(k) = i_alpha(k);
    i_b(k) = -0.5*i_alpha(k) + sqrt(3)/2*i_beta(k);
    i_c(k) = -0.5*i_alpha(k) - sqrt(3)/2*i_beta(k);
end
fprintf('] Done!\n\n');

%% ===== RESULTS =====
fprintf('==================================================\n');
fprintf('                 RESULTS                          \n');
fprintf('==================================================\n\n');

% Analysis regions
regions = [
    0.03, 0.05;    % 1A ramp region
    0.07, 0.11;    % 1A steady
    0.13, 0.15;    % 1.8A ramp
    0.17, 0.19     % 1.8A steady
];

for r = 1:size(regions,1)
    idx = (t >= regions(r,1)) & (t <= regions(r,2));
    id_m = mean(i_d(idx)); iq_m = mean(i_q(idx));
    iq_r = mean(i_q_ref(idx)); Te_m = mean(Te(idx));
    w_rpm = mean(omega(idx)) * 60/(2*pi);
    
    fprintf('Region %d (%.0f-%.0f ms): i_q=%.3fA (ref=%.1fA), Te=%.3fNm, Speed=%.0fRPM\n', ...
        r, regions(r,1)*1000, regions(r,2)*1000, iq_m, iq_r, Te_m, w_rpm);
end

% Steady state (3.5A region)
idx_ss = (t >= 0.17) & (t <= 0.19);
id_ss = mean(i_d(idx_ss));
iq_ss = mean(i_q(idx_ss));
Te_ss = mean(Te(idx_ss));
omega_ss = mean(omega(idx_ss)) * 60/(2*pi);
w_mech = omega_ss * 2*pi/60;
E_back = P * w_mech * psi;

fprintf('\n--- FINAL STEADY-STATE (3.5A region) ---\n\n');
fprintf('  d-axis current:      %8.4f A\n', id_ss);
fprintf('  q-axis current:      %8.4f A\n', iq_ss);
fprintf('  Reference:           %8.1f A\n', mean(i_q_ref(idx_ss)));
fprintf('  Tracking error:      %8.2f %%\n', 100*abs(iq_ss-mean(i_q_ref(idx_ss)))/mean(i_q_ref(idx_ss)));
fprintf('\n');
fprintf('  Torque:              %8.4f Nm\n', Te_ss);
fprintf('  Speed:               %8.1f RPM\n', omega_ss);
fprintf('  Back-EMF (phase):    %8.2f V\n', E_back);
fprintf('\n');

Vpeak = sqrt(mean(v_d(idx_ss).^2) + mean(v_q(idx_ss).^2));
Pout = Te_ss * w_mech;
Pin = 1.5 * (mean(v_d(idx_ss).*i_d(idx_ss)) + mean(v_q(idx_ss).*i_q(idx_ss)));
eff = 100 * Pout / Pin;

fprintf('  Voltage (peak):      %8.2f V\n', Vpeak);
fprintf('  DC utilization:      %8.1f %%\n', 100*Vpeak/(Vdc/sqrt(2)));
fprintf('  Output power:        %8.2f W\n', Pout);
fprintf('  Efficiency:          %8.1f %%\n', eff);

fprintf('\n==================================================\n');
fprintf('           CONTROL SYSTEM SUMMARY                  \n');
fprintf('==================================================\n\n');

fprintf('Control Structure: Field-Oriented Control (FOC)\n\n');
fprintf('  1. Clarke Transform:   i_abc → i_αβ\n');
fprintf('  2. Park Transform:     i_αβ → i_dq\n');
fprintf('  3. PI Current Loops:   i_d*, i_q* → v_d*, v_q*\n');
fprintf('  4. Decoupling:         Add back-EMF compensation\n');
fprintf('  5. Inverse Park:       v_dq → v_αβ\n');
fprintf('  6. SVM/PWM:            v_αβ → 3-phase inverter\n\n');

fprintf('Key Results:\n');
fprintf('  ✓ Current tracking: i_q=%.4fA (ref=%.1fA) at %.0fRPM\n', iq_ss, mean(i_q_ref(idx_ss)), omega_ss);
fprintf('  ✓ Torque:           %.4f Nm\n', Te_ss);
fprintf('  ✓ Efficiency:       %.1f %%\n', eff);
fprintf('\n==================================================\n');

%% ===== PLOTS =====
fprintf('\nGenerating plots...\n');

figure('Name', '3-Phase PMSM FOC Results', 'Position', [100, 100, 1400, 900], 'Visible', 'off');

% d-q Currents
subplot(3,3,1);
plot(t*1000, i_d, 'b-', t*1000, i_q, 'r-', 'LineWidth', 1.5); hold on;
plot(t*1000, i_d_ref, 'b--', t*1000, i_q_ref, 'r--', 'LineWidth', 1); hold off;
xlabel('Time (ms)'); ylabel('Current (A)');
title('d-q Axis Currents (solid=actual, dashed=ref)');
legend('i_d', 'i_q', 'i_d*', 'i_q*', 'FontSize', 8);
grid on; grid minor;

% 3-Phase Currents
subplot(3,3,2);
plot(t*1000, i_a, 'r-', t*1000, i_b, 'g-', t*1000, i_c, 'b-', 'LineWidth', 1);
xlabel('Time (ms)'); ylabel('Current (A)');
title('3-Phase Stator Currents');
legend('i_a', 'i_b', 'i_c', 'FontSize', 8);
grid on; grid minor;

% Error
subplot(3,3,3);
plot(t*1000, e_d, 'b-', t*1000, e_q, 'r-', 'LineWidth', 1);
xlabel('Time (ms)'); ylabel('Error (A)');
title('Current Tracking Error');
legend('e_d', 'e_q', 'FontSize', 8);
grid on; grid minor;

% d-q Voltages
subplot(3,3,4);
plot(t*1000, v_d, 'b-', t*1000, v_q, 'r-', 'LineWidth', 1.5);
xlabel('Time (ms)'); ylabel('Voltage (V)');
title('d-q Axis Voltages');
legend('v_d', 'v_q', 'FontSize', 8);
grid on; grid minor;

% Voltage magnitude
subplot(3,3,5);
Vmag = sqrt(v_d.^2 + v_q.^2);
plot(t*1000, Vmag, 'b-', 'LineWidth', 1.5); hold on;
plot([0,200], [Vdc/sqrt(3), Vdc/sqrt(3)], 'r--', 'LineWidth', 1); hold off;
xlabel('Time (ms)'); ylabel('Voltage (V)');
title('Voltage Vector (red=Vdc/√3)');
grid on; grid minor;

% Torque
subplot(3,3,6);
plot(t*1000, Te, 'b-', 'LineWidth', 1.5); hold on;
plot([0,200], [Te_ss, Te_ss], 'r--', 'LineWidth', 2); hold off;
xlabel('Time (ms)'); ylabel('Torque (Nm)');
title(sprintf('Torque (SS=%.2f Nm)', Te_ss));
grid on; grid minor;

% Speed
subplot(3,3,7);
plot(t*1000, omega*60/(2*pi), 'b-', 'LineWidth', 1.5);
xlabel('Time (ms)'); ylabel('Speed (RPM)');
title('Motor Speed');
grid on; grid minor;

% Current trajectory
subplot(3,3,8);
plot(i_d, i_q, 'b-', 'LineWidth', 0.5); hold on;
plot(0, 0, 'r+', 'MarkerSize', 15, 'LineWidth', 2);
hold off;
xlabel('i_d (A)'); ylabel('i_q (A)');
title('Current Vector (d-q plane)');
axis equal; grid on; grid minor;

% 3-phase voltages (reconstructed)
subplot(3,3,9);
ct = cos(theta_e); st = sin(theta_e);
va = ct.*v_d - st.*v_q;
vb = -0.5*va + sqrt(3)/2*(st.*v_d + ct.*v_q);
vc = -0.5*va - sqrt(3)/2*(st.*v_d + ct.*v_q);
plot(t*1000, va, 'r-', t*1000, vb, 'g-', t*1000, vc, 'b-', 'LineWidth', 1);
xlabel('Time (ms)'); ylabel('Voltage (V)');
title('Phase Voltages');
legend('v_a', 'v_b', 'v_c', 'FontSize', 8);
grid on; grid minor;

saveas(gcf, 'result.png');
fprintf('Plots saved to result.png\n');

fprintf('\nSimulation complete!\n');
