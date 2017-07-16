
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
%Y 电影/用户评分矩阵
%R 用户j是否给电影i打分的矩阵
%合并Y和自己的评分矩阵
Y = [my_ratings Y];
%生成是否打分矩阵
R = zeros(size(Y));
R(Y ~= 0) = 1;

[Ynorm, Ymean] = normalizeRatings(Y, R);

num_users = size(Y, 2);
num_movies = size(Y, 1);
num_features = 10;
%X 电影/特征 矩阵
X = randn(num_movies, num_features);
%Theta 参数矩阵
Theta = randn(num_users, num_features);
%初始化参数
initial_parameters = [X(:); Theta(:)];

options = optimset('GradObj', 'on', 'MaxIter', 100);

lambda = 10;
theta = fmincg (@(t)(cofiCostFunc(t, Y, R, num_users, num_movies, ...
                                num_features, lambda)), ...
                initial_parameters, options);

X = reshape(theta(1:num_movies*num_features), num_movies, num_features);
Theta = reshape(theta(num_movies*num_features+1:end), ...
                num_users, num_features);

fprintf('Recommender system learning completed.\n');



p = X * Theta';
my_predictions = p(:,1) + Ymean;
%载入电影列表
movieList = loadMovieList();
%排序结果
[r, ix] = sort(my_predictions, 'descend');
fprintf('\nTop recommendations for you:\n');
for i=1:10
    j = ix(i);
    fprintf('Predicting rating %.1f for  %s\n', my_predictions(j), ...
            movieList{j});
end
%存储结果
save('recommendids.mat','my_predictions')
%更新Y,R到文件里
save('ex8_movies.mat','Y','R')

