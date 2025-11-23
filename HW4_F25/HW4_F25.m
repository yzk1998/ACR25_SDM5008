n = [0:1:100];
d = (n+1).^(-1);

sy = 0;
for j = 0:100
sy = sy + j*sum(d(j+1:101))
end

ey = sy/101
