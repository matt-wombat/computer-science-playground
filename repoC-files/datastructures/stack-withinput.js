/*

Name: stack-withinput.js

Description: Process number of commands on a stack.

Execute:

  node stack-withinput.js

Expected inputs:

First line: Number of following lines with commands
Commands: push <number>, peek, pop

Example inputs:

5
push 123
push 456
push 789
peek
pop

*/


function execute(program) {
  // initialize the stack
  const stack = [];
  for (const instruction of program) {
      if (instruction == "peek") {
          // print out the top item in stack
          console.log(stack[stack.length - 1]);
      } else if (instruction == "pop") {
          // pop the top item in stack
          stack.pop();
      } else {
          // get the data in the "push" instruction
          const data = parseInt(instruction.substring(5));
          // push data to the top of stack
          stack.push(data);
      }
  }

  return stack;
}

function* main() {
  const programLength = parseInt(yield);
  const program = [];
  for (let i = 0; i < programLength; i++) {
    program.push(yield);
  }
  const res = execute(program);
  console.log(res.join(' '));
}

class EOFError extends Error {}
{
  const gen = main();
  const next = (line) => gen.next(line).done && process.exit();
  let buf = '';
  next();
  process.stdin.setEncoding('utf8');
  process.stdin.on('data', (data) => {
      const lines = (buf + data).split('\r\n');
      buf = lines.pop();
      lines.forEach(next);
  });
  process.stdin.on('end', () => {
      buf && next(buf);
      gen.throw(new EOFError());
  });
}
