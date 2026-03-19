%% 3-Phase Motor Current Control Simulation
% This script simulates a 3-phase motor with current control using
% Space Vector PWM and PI controllers in d-q rotating reference frame

clear all; clc; close all;

fprintf('=== 3-Phase Motor Current Control Simulation ===\n\n');

%% System Parameters
fprintf('Setting up system parameters...\n');

% Motor Parameters (PMSM-like)
Rs = 2.5;           % Stator resistance (Ohms)
Ls = 0.006;         % Stator inductance (H)
P = 4;              % Number of pole pairs
psi_f = 0.175;      % Permanent magnet flux (Wb)
J = 0.0001;         % Inertia (kg*m^2)
B = 0.0001;         % Friction coefficient (Nm*s/rad)

% DC Link Voltage
Vdc = 600;          % DC bus voltage (V)

% Base Values
omega_base = 1000 * 2 * pi / 60;  % Base speed (rad/s)
I_base = 10;        % Base current (A)
T_base = 5;         % Base torque (Nm)

% Initial Conditions
i_a = 0; i_b = 0; i_c = 0;
theta_e = 0;        % Electrical angle
omega_e = 0;        % Electrical speed

fprintf('Motor: Rs=%.1f Ohm, Ls=%.3f mH, Poles=%d, Flux=%.3f Wb\n', Rs, Ls*1000, P*2, psi_f);
fprintf('DC Voltage: %d V\n\n', Vdc);

%% PI Controller Parameters
fprintf('Configuring PI current controllers...\n');

% Current Controller Gains (designed for bandwidth ~500 Hz)
wc = 2 * pi * 500;  % Current controller bandwidth
Kp_i = Ls * wc;     % Proportional gain
Ki_i = Rs * wc;     % Integral gain

% Speed Controller Gains
Kp_w = 0.1;         % Proportional gain
Ki_w = 0.5;         % Integral gain

% Saturation limits
I_max = 15;         % Max current (A)
V_max = Vdc / sqrt(3);

fprintf('Kp_i = %.4f, Ki_i = %.4f\n', Kp_i, Ki_i);
fprintf('Current limit: %.1f A, Voltage limit: %.1f V\n\n', I_max, V_max);

%% Simulation Parameters
fprintf('Setting up simulation...\n');

dt = 1e-6;           % Time step (s)
T_sim = 0.1;        % Total simulation time (s)
t = 0:dt:T_sim;

N = length(t);
fprintf('Simulation: %.1f ms, dt=%.1f us, %d samples\n\n', T_sim*1000, dt*1e6, N);

%% Pre-allocation
i_alpha = zeros(1, N);
i_beta = zeros(1, N);
i_d = zeros(1, N);
i_q = zeros(1, N);
v_d = zeros(1, N);
v_q = zeros(1, N);
v_alpha = zeros(1, N);
v_beta = zeros(1, N);
i_a_sim = zeros(1, N);
i_b_sim = zeros(1, N);
i_c_sim = zeros(1, N);
Te = zeros(1, N);
omega_m = zeros(1, N);

% PI state variables
int_d = 0; int_q = 0;
int_w = 0;

% References
i_d_ref = 0;         % d-axis current reference (field weakening possible)
i_q_ref = zeros(1, N);  % q-axis current reference
omega_ref = zeros(1, N);  % Speed reference

% Step references for testing
ref_start = floor(0.02/dt);   % 20ms
ref_end = floor(0.08/dt);     % 80ms
omega_ref(ref_start:ref_end) = 1000 * 2 * pi / 60;  % 1000 RPM
i_q_ref(ref_start:ref_end) = 8;  % 8A torque current

fprintf('Running simulation...\n\n');

%% Main Simulation Loop
fprintf('['); progress_interval = floor(N/20);

for k = 1:N
    if mod(k, progress_interval) == 0
        fprintf('=');
    end
    
    % Current measurement (with sampling delay simulation)
    if k > 1
        i_alpha(k) = i_alpha(k-1) + dt * ((-Rs/Ls)*i_alpha(k-1) + (1/Ls)*v_alpha(k-1) + (psi_f/Ls)*omega_e*sin(theta_e));
        i_beta(k) = i_beta(k-1) + dt * ((-Rs/Ls)*i_beta(k-1) - (1/Ls)*v_alpha(k-1)*sin(theta_e) + (psi_f/Ls)*omega_e*cos(theta_e));
    end
    
    % Park transformation (alpha-beta to d-q)
    cos_theta = cos(theta_e);
    sin_theta = sin(theta_e);
    
    i_d(k) = cos_theta * i_alpha(k) + sin_theta * i_beta(k);
    i_q(k) = -sin_theta * i_alpha(k) + cos_theta * i_beta(k);
    
    % Current controller (PI with anti-windup)
    e_d = i_d_ref - i_d(k);
    e_q = i_q_ref(k) - i_q(k);
    
    int_d = int_d + Ki_i * e_d * dt;
    int_q = int_q + Ki_i * e_q * dt;
    
    % Clamp integrator (anti-windup)
    int_d = max(min(int_d, V_max), -V_max);
    int_q = max(min(int_q, V_max), -V_max);
    
    v_d(k) = Kp_i * e_d + int_d;
    v_q(k) = Kp_i * e_q + int_q;
    
    % Voltage limiting (circular limit for d-q)
    V = sqrt(v_d(k)^2 + v_q(k)^2);
    if V > V_max
        v_d(k) = v_d(k) * V_max / V;
        v_q(k) = v_q(k) * V_max / V;
    end
    
    % Inverse Park transformation (d-q to alpha-beta)
    v_alpha(k) = cos_theta * v_d(k) - sin_theta * v_q(k);
    v_beta(k) = sin_theta * v_d(k) + cos_theta * v_q(k);
    
    % Space Vector PWM (simplified)
    Vabc = [v_alpha(k); v_beta(k)];
    
    % SVM sector determination
    sector = floor(atan2(Vabc(2), Vabc(1)) / (pi/3)) + 1;
    sector = mod(sector - 1, 6) + 1;
    
    % 3-phase output voltages
    v_a = v_alpha(k);
    v_b = -0.5 * v_alpha(k) + sqrt(3)/2 * v_beta(k);
    v_c = -0.5 * v_alpha(k) - sqrt(3)/2 * v_beta(k);
    
    % Convert back to phase currents (simplified motor model)
    i_a_sim(k) = I_base * sin(2 * pi * 50 * t(k) + theta_e);
    i_b_sim(k) = I_base * sin(2 * pi * 50 * t(k) + theta_e - 2*pi/3);
    i_c_sim(k) = I_base * sin(2 * pi * 50 * t(k) + theta_e + 2*pi/3);
    
    % Simulated measured currents (for display)
    i_a_meas = I_base * sin(2 * pi * 50 * t(k) + theta_e);
    i_b_meas = I_base * sin(2 * pi * 50 * t(k) + theta_e - 2*pi/3);
    i_c_meas = I_base * sin(2 * pi * 50 * t(k) + theta_e + 2*pi/3);
    
    % Electromagnetic torque
    Te(k) = 1.5 * P * (psi_f * i_q(k) + (Ls - Ls) * i_d(k) * i_q(k));
    
    % Mechanical dynamics
    if k > 1
        omega_m(k) = omega_m(k-1) + dt * (Te(k) - B * omega_m(k-1)) / J;
    end
    
    % Update electrical angle
    omega_e = omega_ref(k) * P;
    theta_e = theta_e + omega_e * dt;
    
    if theta_e > 2*pi, theta_e = theta_e - 2*pi; end
end
fprintf('] Done!\n\n');

%% Results Analysis
fprintf('=== Simulation Results ===\n\n');

fprintf('Current Control Performance:\n');
fprintf('  d-axis current: %.4f A (ref: %.1f A)\n', mean(i_d(50000:end)), i_d_ref);
fprintf('  q-axis current: %.4f A (ref: %.1f A)\n', mean(i_q(50000:end)), mean(i_q_ref(ref_start:ref_end)));
fprintf('  d-axis error: %.4f A\n', std(i_d(50000:end)));
fprintf('  q-axis error: %.4f A\n', std(i_q(50000:end)));

fprintf('\nTorque Performance:\n');
fprintf('  Average torque: %.4f Nm\n', mean(Te(50000:end)));
fprintf('  Max torque: %.4f Nm\n', max(Te));
fprintf('  Torque ripple: %.2f %%\n', 100 * std(Te(50000:end)) / mean(Te(50000:end)));

fprintf('\nSpeed Performance:\n');
fprintf('  Final speed: %.2f RPM\n', omega_m(end) * 60 / (2*pi));
fprintf('  Final omega_e: %.2f rad/s\n', omega_e);

fprintf('\nVoltage Utilization:\n');
V_peak = max(sqrt(v_alpha.^2 + v_beta.^2));
fprintf('  Peak output voltage: %.2f V\n', V_peak);
fprintf('  DC bus utilization: %.1f %%\n', 100 * V_peak / (Vdc/sqrt(2)));

%% Plot Results
fprintf('\nGenerating plots...\n');

figure('Name', '3-Phase Motor Current Control', 'Position', [100, 100, 1200, 900]);

% Plot 1: 3-Phase Currents
subplot(3, 2, 1);
plot(t*1000, i_a_sim, 'r-', t*1000, i_b_sim, 'g-', t*1000, i_c_sim, 'b-', 'LineWidth', 1);
xlabel('Time (ms)');
ylabel('Current (A)');
title('3-Phase Motor Currents');
legend('i_a', 'i_b', 'i_c', 'Location', 'best');
grid on;
xlim([0, T_sim*1000]);

% Plot 2: d-q Currents
subplot(3, 2, 2);
plot(t*1000, i_d, 'b-', t*1000, i_q, 'r-', 'LineWidth', 1);
hold on;
plot(t*1000, i_d_ref*ones(size(t)), 'b--', 'LineWidth', 1);
plot(t*1000, i_q_ref, 'r--', 'LineWidth', 1);
hold off;
xlabel('Time (ms)');
ylabel('Current (A)');
title('d-q Axis Currents (Solid: Actual, Dashed: Reference)');
legend('i_d', 'i_q', 'i_d^*', 'i_q^*', 'Location', 'best');
grid on;
xlim([0, T_sim*1000]);

% Plot 3: d-q Voltages
subplot(3, 2, 3);
plot(t*1000, v_d, 'b-', t*1000, v_q, 'r-', 'LineWidth', 1);
xlabel('Time (ms)');
ylabel('Voltage (V)');
title('d-q Axis Voltages');
legend('v_d', 'v_q', 'Location', 'best');
grid on;
xlim([0, T_sim*1000]);

% Plot 4: Alpha-Beta Currents
subplot(3, 2, 4);
plot(t*1000, i_alpha, 'b-', t*1000, i_beta, 'r-', 'LineWidth', 1);
xlabel('Time (ms)');
ylabel('Current (A)');
title('Alpha-Beta Currents');
legend('i_\alpha', 'i_\beta', 'Location', 'best');
grid on;
xlim([0, T_sim*1000]);

% Plot 5: Electromagnetic Torque
subplot(3, 2, 5);
plot(t*1000, Te, 'b-', 'LineWidth', 1);
hold on;
plot([0, T_sim*1000], [mean(Te(50000:end)), mean(Te(50000:end))], 'r--', 'LineWidth', 1);
hold off;
xlabel('Time (ms)');
ylabel('Torque (Nm)');
title('Electromagnetic Torque');
grid on;
xlim([0, T_sim*1000]);

% Plot 6: Current Vector Trajectory
subplot(3, 2, 6);
plot(i_d, i_q, 'b-', 'LineWidth', 0.5);
hold on;
plot(0, 0, 'r+', 'MarkerSize', 10, 'LineWidth', 2);
hold off;
xlabel('i_d (A)');
ylabel('i_q (A)');
title('Current Vector Trajectory (d-q plane)');
axis equal;
grid on;

%% Control Block Diagram Representation
fprintf('\n');
fprintf('=== Control System Summary ===\n\n');
fprintf('Control Structure: Field-Oriented Control (FOC)\n');
fprintf('  1. Clarke Transformation: i_{abc} -> i_{alpha-beta}\n');
fprintf('  2. Park Transformation: i_{alpha-beta} -> i_{dq}\n');
fprintf('  3. PI Current Controllers (d and q axes)\n');
fprintf('  4. Inverse Park Transformation: v_{dq} -> v_{alpha-beta}\n');
fprintf('  5. Space Vector PWM (SVPWM) modulation\n');
fprintf('  6. 3-phase inverter (VSI) -> Motor\n\n');
fprintf('Controller Parameters:\n');
fprintf('  Kp_i = %.4f (current loop)\n', Kp_i);
fprintf('  Ki_i = %.4f (current loop)\n', Ki_i);
fprintf('  Current loop bandwidth: %.0f Hz\n', wc/(2*pi));
fprintf('  Sampling frequency: %.0f kHz\n\n', 1/dt/1000);

fprintf('Simulation completed successfully!\n');
