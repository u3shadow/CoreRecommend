
load ('ex8_movies.mat');

movieList = loadMovieList();
%读取打分矩阵
load('my_ratting.mat')

fprintf('\n\nNew user ratings:\n');
for i = 1:length(my_ratings)
    if my_ratings(i) > 0 
        fprintf('Rated %d for %s\n', my_ratings(i), ...
                 movieList{i});
    end
end


fprintf('\nTraining collaborative filtering...\n');

%  Load data 获得Y,R
load('ex8_movies.mat');
%Y 电影/特征矩阵
%R 用户j是否给电影i打分的矩阵
%生成是否打分矩阵
R = zeros(size(my_ratings));
R(my_ratings ~= 0) = 1;

num_movies = size(Y, 1);
%Theta 参数矩阵
Theta = randn(1,338);
%初始化参数
initial_parameters = Theta(:);

options = optimset('GradObj', 'on', 'MaxIter', 400);

lambda = 10;
[x,output] = fminunc (@(t)(costFunc(Y,my_ratings, R,...
                                t, lambda)), ...
                initial_parameters, options);
 theta = x;
 my_predictions = Y*theta;
 my_predictions = my_predictions';
%载入电影列表
movieList = loadMovieList();
%排序结果
[r, ix] = sort(my_predictions, 'descend');
fprintf('\nTop recommendations for you:\n');
result = cell(10,1);
for i=1:10
    j = ix(i);
    fprintf('Predicting rating %.1f for  %s\n', my_predictions(j), ...
            movieList{j});
    result{i} = j;
end
save result.txt result

