function PSNR = calcPSNR(x1,x2,maxX)

if nargin == 2
maxX = 1; 
end
if calcMSE(x1,x2) == 0
    PSNR = 100;
else
    PSNR = 10*(log10(((maxX)^2)./(calcMSE(x1,x2))));
end
end
    