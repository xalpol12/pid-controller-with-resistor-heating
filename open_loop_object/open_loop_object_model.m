clc; clear all; close all;

data_filename = '';
temperature = load(data_filename);
dt = 1; %sample time
samples = length(temperature);
t = (0:samples-1)*dt;

%Input sig
input_amplitude = 0.9;
input = input_amplitude*ones(1, samples);

%LTI model
s = tf('s');
k = 8.65/input_amplitude; %model gain -> modify
T = 300; %model time constant -> modify
delay = 10; %model delay -> modify
H = k/(1+s*T)*exp(-s*delay); %model
fprintf('Model parameters k=%.2g, T=%g, delay=%g\n', k, T, delay);

%Model response
system_offset = 22.95;
model_response = lsim(H,input,t);
model_response = model_response + system_offset; %add offset

%Model error
residuum = temperature - model_response';
error_abs_sum = sum(abs(residuum));
fprintf('Model error sum(abs(residuum)) = %g\n\n', error_abs_sum);

figure;
plot(t,temperature, '.', t, model_response, '.');
title('Real object and model');
xlabel('Time (s)');
ylabel('Temperature (C)');
legend('measurement samples', 'model reponse of heater+BMP280');
axis tight;
grid minor;

figure;
plot(t,residuum, '.');
title('Residuum (measurement samples - model reponse)');
xlabel('Time (s)');
ylabel('Temperature (C)');
axis tight;
ylim([-0.5 0.5]);
grid minor;