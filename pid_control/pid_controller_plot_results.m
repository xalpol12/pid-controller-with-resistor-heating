data_filename = 'pid_measurements.txt';
data_filename_2 = 'u_measurements.txt';
temperature = load(data_filename);
u = load(data_filename_2) * 100;
dt = 1;
number_of_samples = length(temperature);
t = (0:number_of_samples-1)*dt;
set_point = 27.5;


subplot(2,1,1);
plot(t,temperature, 'b.');
hold on;
line([0 t(end)],[set_point, set_point],'Color','red','LineStyle','--');
hold off;
title('PI controller, Kp=0.6073, Ki=0.0024, Kd=0');
xlabel('Time (s)');
ylabel('Temperature (C)');
legend('measurement samples');
axis tight;
grid minor;
subplot(2,1,2);
title('PWM Duty');
plot(t, u, 'b.');
xlabel('Time (s)');
ylabel('DUTY [%]');
legend('U measured');
axis tight;
grid minor;
