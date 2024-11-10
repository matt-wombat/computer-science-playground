function factorial(num) {
  if (num == 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  };
};

function fibonacci(num) {
  if (num <= 1) {
    return num;
  } else {
    return fibonacci(num-1) + fibonacci(num-2);
  };
};

// Export for modularization
module.exports.factorial = factorial;
module.exports.fibonacci = fibonacci;

