function sum()
    local sum1 = 0
    local sum2 = 0
    for i = 1, 100 do
        sum1 = sum1 + (i * i)
        sum2 = sum2 + i
    end
    return (sum2 * sum2) - sum1
end

if arg and arg[0] == "p006.lua" then
    print(sum())
end
