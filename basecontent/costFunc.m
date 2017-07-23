function [J,grad] = costFunc(X, Y, R, Theta, lambda)
nm = length(Y(:,1));
nt = length(Theta);
sum = 0;
for i=1:nm
    if R(i) == 1
       sum =sum + (Theta'*X(i,:)' - Y(i))*(Theta'*X(i,:)' - Y(i));
    end
end
sum = sum/2;
sum1 = 0;
for j=1:nt
    sum1 = sum1 + Theta(j)*Theta(j);
end
sum1 = sum1*lambda/2;
J = sum + sum1;
grad = 0;
for k=1:nm
    if R(k) == 1
       grad =grad + (Theta'*X(k,:)' - Y(k))*X(k,:);
    end
end
grad = grad';
end
