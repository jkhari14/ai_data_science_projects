function vecOut = makeVector(matrixIn)

if isnumeric(matrixIn) ~= 1
    error('Inputed matrix has to consist of numeric values')
elseif ndims(matrixIn) > 2
    error('The dimension of the input matrix exceeds 2')
else
vecOut = reshape(matrixIn,[],1);
end
end
