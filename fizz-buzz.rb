def fizz_buzz(n)
  1.upto(n).map do |x|
    x % 3 == 0 ? x % 5 == 0 ? "FizzBuzz" : "Fizz" : x % 5 == 0 ? "Buzz" : x.to_s
  end
end

puts fizz_buzz(15)
