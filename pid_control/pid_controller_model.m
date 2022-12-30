clc; clear all; close all;

%model
input_amplitude = 0.9;
set_point = 26;

s = tf('s');
k = 8.65/input_amplitude; %model gain -> modify
T = 300; %model time constant -> modify
delay = 10; %model delay -> modify
H = k/(1+s*T)*exp(-s*delay); %model

%controller params
dt = 1;
kp = 0.93;
ki = 0.0039;
kd = 0;

%plotting variables
system_offset = 22.95;