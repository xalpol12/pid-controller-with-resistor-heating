clc; clear all; close all;

%model
input_amplitude = 0.9;

s = tf('s');
k = 8.65/input_amplitude; %model gain -> modify
T = 300; %model time constant -> modify
delay = 10; %model delay -> modify
H = k/(1+s*T)*exp(-s*delay); %model

%controller params
Hist = 0.5;
u_max = 1;
u_min = 0;

%plotting variables
system_offset = 22.95;