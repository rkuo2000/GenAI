classdef MCPServer
    properties
        running = false;
        requestId = 0;
    end
    
    methods
        function obj = MCPServer()
            obj.running = false;
        end
        
        function start(obj)
            if obj.running
                warning('MCP Server already running');
                return;
            end
            obj.running = true;
            fprintf('[MCP Server] Started on stdio\n');
            obj.runLoop();
        end
        
        function stop(obj)
            obj.running = false;
            fprintf('[MCP Server] Stopped\n');
        end
        
        function runLoop(obj)
            while obj.running
                try
                    line = fgetl(stdin);
                    if ~ischar(line) || strcmp(line, '-1')
                        break;
                    end
                    line = strtrim(line);
                    if isempty(line)
                        continue;
                    end
                    
                    obj.handleRequest(line);
                catch ME
                    obj.sendError([], -32603, ME.message);
                end
            end
        end
        
        function handleRequest(obj, jsonStr)
            try
                data = jsondecode(jsonStr);
                if ~isfield(data, 'jsonrpc') || ~strcmp(data.jsonrpc, '2.0')
                    obj.sendError([], -32600, 'Invalid JSON-RPC version');
                    return;
                end
                
                method = data.method;
                params = struct();
                if isfield(data, 'params')
                    params = data.params;
                end
                reqId = [];
                if isfield(data, 'id')
                    reqId = data.id;
                end
                
                switch method
                    case 'initialize'
                        obj.sendResponse(reqId, struct( ...
                            'protocolVersion', '0.1.0', ...
                            'serverInfo', struct('name', 'matlab-mcp', 'version', '1.0.0'), ...
                            'capabilities', struct('tools', true, 'resources', false) ...
                        ));
                    
                    case 'tools/list'
                        tools = obj.listTools();
                        obj.sendResponse(reqId, struct('tools', tools));
                    
                    case 'tools/call'
                        result = obj.callTool(params.name, params.arguments);
                        obj.sendResponse(reqId, struct('content', {{struct('type', 'text', 'text', result)}}));
                    
                    case 'shutdown'
                        obj.sendResponse(reqId, struct());
                        obj.running = false;
                    
                    otherwise
                        obj.sendError(reqId, -32601, sprintf('Method not found: %s', method));
                end
            catch ME
                obj.sendError([], -32700, sprintf('Parse error: %s', ME.message));
            end
        end
        
        function tools = listTools(obj)
            tools = struct( ...
                'name', 'matlab_eval', ...
                'description', 'Evaluate MATLAB expression or command', ...
                'inputSchema', struct( ...
                    'type', 'object', ...
                    'properties', struct( ...
                        'expression', struct('type', 'string', 'description', 'MATLAB expression or command to evaluate') ...
                    ), ...
                    'required', {{'expression'}} ...
                ) ...
            );
            
            tools(2) = struct( ...
                'name', 'matlab_workspace', ...
                'description', 'Get all variables in the MATLAB workspace', ...
                'inputSchema', struct( ...
                    'type', 'object', ...
                    'properties', struct() ...
                ) ...
            );
            
            tools(3) = struct( ...
                'name', 'matlab_load', ...
                'description', 'Load variables from a .mat file', ...
                'inputSchema', struct( ...
                    'type', 'object', ...
                    'properties', struct( ...
                        'filename', struct('type', 'string', 'description', 'Path to .mat file') ...
                    ), ...
                    'required', {{'filename'}} ...
                ) ...
            );
            
            tools(4) = struct( ...
                'name', 'matlab_save', ...
                'description', 'Save variables to a .mat file', ...
                'inputSchema', struct( ...
                    'type', 'object', ...
                    'properties', struct( ...
                        'filename', struct('type', 'string', 'description', 'Path to .mat file'), ...
                        'variables', struct('type', 'array', 'description', 'Variable names to save (empty for all)'), ...
                        'append', struct('type', 'boolean', 'description', 'Append to existing file') ...
                    ), ...
                    'required', {{'filename'}} ...
                ) ...
            );
            
            tools(5) = struct( ...
                'name', 'matlab_plot', ...
                'description', 'Create a plot with data', ...
                'inputSchema', struct( ...
                    'type', 'object', ...
                    'properties', struct( ...
                        'x', struct('type', 'array', 'description', 'X data'), ...
                        'y', struct('type', 'array', 'description', 'Y data'), ...
                        'type', struct('type', 'string', 'description', 'Plot type: plot, scatter, bar, stem'), ...
                        'title', struct('type', 'string', 'description', 'Plot title'), ...
                        'xlabel', struct('type', 'string', 'description', 'X-axis label'), ...
                        'ylabel', struct('type', 'string', 'description', 'Y-axis label') ...
                    ), ...
                    'required', {{'x', 'y'}} ...
                ) ...
            );
            
            tools(6) = struct( ...
                'name', 'matlab_control_sim', ...
                'description', 'Simulate a control system response', ...
                'inputSchema', struct( ...
                    'type', 'object', ...
                    'properties', struct( ...
                        'num', struct('type', 'array', 'description', 'Numerator coefficients'), ...
                        'den', struct('type', 'array', 'description', 'Denominator coefficients'), ...
                        'tfinal', struct('type', 'number', 'description', 'Final time'), ...
                        'input_type', struct('type', 'string', 'description', 'Input type: step, impulse') ...
                    ), ...
                    'required', {{'num', 'den'}} ...
                ) ...
            );
            
            tools(7) = struct( ...
                'name', 'matlab_pid_tune', ...
                'description', 'Design a PID controller', ...
                'inputSchema', struct( ...
                    'type', 'object', ...
                    'properties', struct( ...
                        'plant_num', struct('type', 'array', 'description', 'Plant numerator'), ...
                        'plant_den', struct('type', 'array', 'description', 'Plant denominator'), ...
                        'Kp', struct('type', 'number', 'description', 'Proportional gain'), ...
                        'Ki', struct('type', 'number', 'description', 'Integral gain'), ...
                        'Kd', struct('type', 'number', 'description', 'Derivative gain') ...
                    ), ...
                    'required', {{'plant_num', 'plant_den'}} ...
                ) ...
            );
            
            tools(8) = struct( ...
                'name', 'matlab_bode', ...
                'description', 'Generate Bode plot data', ...
                'inputSchema', struct( ...
                    'type', 'object', ...
                    'properties', struct( ...
                        'num', struct('type', 'array', 'description', 'Numerator coefficients'), ...
                        'den', struct('type', 'array', 'description', 'Denominator coefficients'), ...
                        'w_range', struct('type', 'array', 'description', 'Frequency range [wmin wmax]') ...
                    ), ...
                    'required', {{'num', 'den'}} ...
                ) ...
            );
            
            tools(9) = struct( ...
                'name', 'matlab_nyquist', ...
                'description', 'Generate Nyquist plot data', ...
                'inputSchema', struct( ...
                    'type', 'object', ...
                    'properties', struct( ...
                        'num', struct('type', 'array', 'description', 'Numerator coefficients'), ...
                        'den', struct('type', 'array', 'description', 'Denominator coefficients') ...
                    ), ...
                    'required', {{'num', 'den'}} ...
                ) ...
            );
            
            tools(10) = struct( ...
                'name', 'matlab_lsim', ...
                'description', 'Simulate linear system response to arbitrary input', ...
                'inputSchema', struct( ...
                    'type', 'object', ...
                    'properties', struct( ...
                        'num', struct('type', 'array', 'description', 'Numerator coefficients'), ...
                        'den', struct('type', 'array', 'description', 'Denominator coefficients'), ...
                        'u', struct('type', 'array', 'description', 'Input signal'), ...
                        't', struct('type', 'array', 'description', 'Time vector') ...
                    ), ...
                    'required', {{'num', 'den', 'u', 't'}} ...
                ) ...
            );
        end
        
        function result = callTool(obj, toolName, args)
            switch toolName
                case 'matlab_eval'
                    result = obj.matlabEval(args.expression);
                    
                case 'matlab_workspace'
                    result = obj.getWorkspace();
                    
                case 'matlab_load'
                    result = obj.loadVariables(args.filename);
                    
                case 'matlab_save'
                    vars = {};
                    if isfield(args, 'variables') && ~isempty(args.variables)
                        vars = args.variables;
                    end
                    append = false;
                    if isfield(args, 'append')
                        append = args.append;
                    end
                    result = obj.saveVariables(args.filename, vars, append);
                    
                case 'matlab_plot'
                    result = obj.createPlot(args);
                    
                case 'matlab_control_sim'
                    tfinal = 10;
                    inputType = 'step';
                    if isfield(args, 'tfinal'), tfinal = args.tfinal; end
                    if isfield(args, 'input_type'), inputType = args.input_type; end
                    result = obj.controlSim(args.num, args.den, tfinal, inputType);
                    
                case 'matlab_pid_tune'
                    Kp = 1; Ki = 0; Kd = 0;
                    if isfield(args, 'Kp'), Kp = args.Kp; end
                    if isfield(args, 'Ki'), Ki = args.Ki; end
                    if isfield(args, 'Kd'), Kd = args.Kd; end
                    result = obj.pidTune(args.plant_num, args.plant_den, Kp, Ki, Kd);
                    
                case 'matlab_bode'
                    wRange = [];
                    if isfield(args, 'w_range'), wRange = args.w_range; end
                    result = obj.bodePlot(args.num, args.den, wRange);
                    
                case 'matlab_nyquist'
                    result = obj.nyquistPlot(args.num, args.den);
                    
                case 'matlab_lsim'
                    result = obj.lsim(args.num, args.den, args.u, args.t);
                    
                otherwise
                    result = sprintf('Unknown tool: %s', toolName);
            end
        end
        
        function result = matlabEval(obj, expr)
            try
                result = evalc(expr);
                if isempty(strtrim(result))
                    result = 'Expression evaluated successfully (no output)';
                end
            catch ME
                result = sprintf('Error: %s', ME.message);
            end
        end
        
        function result = getWorkspace(obj)
            w = whos;
            if isempty(w)
                result = 'Workspace is empty';
                return;
            end
            lines = cell(1, length(w));
            for i = 1:length(w)
                lines{i} = sprintf('%s (%s, %dx%d)', w(i).name, w(i).class, w(i).size(1), w(i).size(2));
            end
            result = sprintf('Workspace variables:\n%s', strjoin(lines, '\n'));
        end
        
        function result = loadVariables(obj, filename)
            try
                data = load(filename);
                vars = fieldnames(data);
                for i = 1:length(vars)
                    assignin('base', vars{i}, data.(vars{i}));
                end
                result = sprintf('Loaded %d variable(s) from %s', length(vars), filename);
            catch ME
                result = sprintf('Error loading %s: %s', filename, ME.message);
            end
        end
        
        function result = saveVariables(obj, filename, vars, append)
            try
                if isempty(vars)
                    evalin('base', sprintf('save(''%s'')', filename));
                elseif append
                    evalin('base', sprintf('save(''%s'', ''%s'', ''-append'')', filename, strjoin(vars, ''', ''')));
                else
                    evalin('base', sprintf('save(''%s'', ''%s'')', filename, strjoin(vars, ''', ''')));
                end
                result = sprintf('Variables saved to %s', filename);
            catch ME
                result = sprintf('Error saving: %s', ME.message);
            end
        end
        
        function result = createPlot(obj, args)
            try
                x = cell2mat(args.x(:));
                y = cell2mat(args.y(:));
                
                plotType = 'plot';
                if isfield(args, 'type'), plotType = args.type; end
                
                figure('Visible', 'off');
                switch plotType
                    case 'scatter'
                        scatter(x, y);
                    case 'bar'
                        bar(x, y);
                    case 'stem'
                        stem(x, y);
                    otherwise
                        plot(x, y);
                end
                
                if isfield(args, 'title'), title(args.title); end
                if isfield(args, 'xlabel'), xlabel(args.xlabel); end
                if isfield(args, 'ylabel'), ylabel(args.ylabel); end
                grid on;
                
                result = 'Plot created successfully';
            catch ME
                result = sprintf('Error creating plot: %s', ME.message);
            end
        end
        
        function result = controlSim(obj, num, den, tfinal, inputType)
            try
                sys = tf(cell2mat(num), cell2mat(den));
                
                if strcmp(inputType, 'impulse')
                    [y, t] = impulse(sys, tfinal);
                    inputLabel = 'Impulse';
                else
                    [y, t] = step(sys, tfinal);
                    inputLabel = 'Step';
                end
                
                result = sprintf('%s response generated:\nTime range: 0 to %.2f\nFinal value: %.4f\nPeak value: %.4f', ...
                    inputLabel, tfinal, y(end), max(y));
            catch ME
                result = sprintf('Error in control simulation: %s', ME.message);
            end
        end
        
        function result = pidTune(obj, plantNum, plantDen, Kp, Ki, Kd)
            try
                plant = tf(cell2mat(plantNum), cell2mat(plantDen));
                controller = pid(Kp, Ki, Kd);
                closedLoop = feedback(controller * plant, 1);
                
                [y, t] = step(closedLoop, 10);
                
                info = stepinfo(closedLoop);
                
                result = sprintf('PID Controller Closed-Loop Response:\nKp=%.4f, Ki=%.4f, Kd=%.4f\nRise Time: %.4f s\nSettling Time: %.4f s\nOvershoot: %.2f%%\nFinal Value: %.4f', ...
                    Kp, Ki, Kd, info.RiseTime, info.SettlingTime, info.Overshoot, y(end));
            catch ME
                result = sprintf('Error in PID tuning: %s', ME.message);
            end
        end
        
        function result = bodePlot(obj, num, den, wRange)
            try
                sys = tf(cell2mat(num), cell2mat(den));
                
                if isempty(wRange)
                    w = logspace(-2, 2, 500);
                else
                    w = logspace(log10(wRange(1)), log10(wRange(2)), 500);
                end
                
                [mag, phase, w] = bode(sys, w);
                mag = squeeze(mag);
                phase = squeeze(phase);
                
                [GM, PM, wg, wp] = margin(sys);
                
                result = sprintf('Bode plot data generated:\nGain crossover: %.4f rad/s\nPhase crossover: %.4f rad/s\nGain Margin: %.4f (%.2f dB)\nPhase Margin: %.4f deg', ...
                    wp, wg, GM, 20*log10(GM), PM);
            catch ME
                result = sprintf('Error generating Bode plot: %s', ME.message);
            end
        end
        
        function result = nyquistPlot(obj, num, den)
            try
                sys = tf(cell2mat(num), cell2mat(den));
                
                [re, im, w] = nyquist(sys);
                re = squeeze(re);
                im = squeeze(im);
                
                result = sprintf('Nyquist plot data generated:\nPoints: %d\nReal range: [%.4f, %.4f]\nImag range: [%.4f, %.4f]', ...
                    length(w), min(re), max(re), min(im), max(im));
            catch ME
                result = sprintf('Error generating Nyquist plot: %s', ME.message);
            end
        end
        
        function result = lsim(obj, num, den, u, t)
            try
                sys = tf(cell2mat(num), cell2mat(den));
                u = cell2mat(u(:));
                t = cell2mat(t(:));
                
                [y, t_out, x] = lsim(sys, u, t);
                
                result = sprintf('Linear simulation complete:\nSamples: %d\nTime range: [%.4f, %.4f]\nOutput range: [%.4f, %.4f]', ...
                    length(t), t(1), t(end), min(y), max(y));
            catch ME
                result = sprintf('Error in lsim: %s', ME.message);
            end
        end
        
        function sendResponse(obj, id, result)
            resp.id = id;
            resp.jsonrpc = '2.0';
            resp.result = result;
            fprintf('%s\n', jsonencode(resp));
            drawnow;
        end
        
        function sendError(obj, id, code, message)
            err.id = id;
            err.jsonrpc = '2.0';
            err.error.code = code;
            err.error.message = message;
            fprintf('%s\n', jsonencode(err));
            drawnow;
        end
    end
end
