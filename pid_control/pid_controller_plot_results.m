data_filename = '';
temperature = load(data_filename);
dt = 1;
number_of_samples = length(temperature);
t = (0:number_of_samples-1)*dt;
set_point = 26;

figure(1);
plot(t,temperature, 'b.');
hold on;
line([0 t(end)],[set_point, set_point],'Color','red','LineStyle','--');
hold off;
title('PI controller, Kp=1.2, Ki=0.002, Kd=0');
xlabel('Time (s)');
ylabel('Temperature (C)');
legend('measurement samples');
axis tight;
grid minor;