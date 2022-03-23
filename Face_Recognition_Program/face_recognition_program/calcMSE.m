function MSE = calcMSE(x1,x2) 

x1 = makeVector(x1);
x2 = makeVector(x2);

if length(x1) ~= length(x2)
    error('The lengths of the vectors or the vectorized lengths of the given matrices do not match')
else
MSE = (1/length(x1))*(sum((x1 - x2).^2));
% sum((1/length(x1))*((x1 - x2).^2))
end
end