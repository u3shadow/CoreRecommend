function movieList = loadMovieList()
%GETMOVIELIST reads the fixed movie list in movie.txt and returns a
%cell array of the words
%   movieList = GETMOVIELIST() reads the fixed movie list in movie.txt 
%   and returns a cell array of the words in movieList.


%% Read the fixed movieulary list
pkg load database;
conn = pq_connect (setdbopts ("dbname", "redb"));
data = pq_exec_params (conn, "select * from games;").data;
nums = pq_exec_params (conn, "select count(*) from games;").data;
nums = cell2mat(nums);
% Store all movies in cell array movie{}
n = nums;  % Total number of movies
movieList = cell(n, 1);
for i = 1:n
    movieList{i} = cell2mat(data(i,2));
end
pkg unload database;
end
