function plotIndices(scrambledIndices, correctIndices)

figure()

x = correctIndices;
y = scrambledIndices;
subplot(1,2,1)
plot(x,y,'o')
xlim([0,length(scrambledIndices)])
ylim([0,length(scrambledIndices)])
title('Scrambled Indices')
xlabel('Player ID')
ylabel('Database Column')
axis square

a = correctIndices;
b = correctIndices;
subplot(1,2,2)
plot(a,b,'o')
xlim([0,length(correctIndices)])
ylim([0,length(correctIndices)])
title('Correct Indices')
xlabel('Player ID')
ylabel('Database Column')
axis square