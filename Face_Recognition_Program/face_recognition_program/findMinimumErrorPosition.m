function minPos = findMinimumErrorPosition(imgVec, imageDatabase)

MSE_vec = zeros(1,size(imageDatabase,2));
for ii = 1:size(imageDatabase,2)
    MSE_vec(1,ii) = calcMSE(imgVec,imageDatabase(:,ii));
end
 minPos = find(MSE_vec == min(MSE_vec,[],'all'));



% MSE_vec = (MSE_vec == min(MSE_vec,[],'all'));
% minPos = find(MSE_vec);