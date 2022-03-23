function PSNRs = computePSNRs(imgVec, imageDatabase)

PSNRs = zeros(1,size(imageDatabase,2));
for ii = 1:size(imageDatabase,2)
PSNRs(1,ii) = calcPSNR(imgVec,imageDatabase(:,ii));
end
