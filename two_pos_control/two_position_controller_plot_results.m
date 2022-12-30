data_filename = '';
temperature = load(data_filename);
dt = 1; %sample time
samples = length(temperature);
t = (0:samples-1)*dt;

set_point = 26;
histeresis = 0.5;

figure;
plot(t,temperature, 'b.');
hold on;
line([0 t(end)],[set_point, set_point],'Color','green','LineStyle','--');
line([0 t(end)],[set_point+histeresis/2, set_point+histeresis/2],'Color','red','LineStyle','--');
line([0 t(end)],[set_point-histeresis/2, set_point-histeresis/2],'Color','red','LineStyle','--');
hold off;
title('Two position controller');
xlabel('Time (s)');
ylabel('Temperature (C)');
legend('measurement samples');
axis tight;
grid minor;