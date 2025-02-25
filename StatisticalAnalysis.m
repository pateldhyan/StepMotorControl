%% Load Data
load 'SampleDataSets/StatisticalAnalysis.mat'

%% Power Analysis
sampleData = PowerAnalysisData;

%Enter desired speed in [cm/s]
h0_mean = 44;

experimental_mean = mean(sampleData);
experimental_std = std(sampleData);

numbertrialsexperimental  = sampsizepwr('t', [h0_mean experimental_std], experimental_mean);


%% Statistical Analysis

%Enter name of measured dataset
measuredData_time = measuredRawData1;

phantomDiameter = 17;   % in cm

% Converting time of 10 rotations into linear speed of surface
measuredData = (1./(measuredData_time/10)).*(2*3.14159265).*(phantomDiameter/2);

% Enter hypothesized mean
hypothesized_mean = 44;

h = ttest(measuredData, hypothesized_mean);