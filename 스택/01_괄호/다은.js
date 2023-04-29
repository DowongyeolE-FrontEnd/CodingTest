function solution(n, strings) {
  for (let i = 0; i < n; i++) {
    const string = strings[i].split("");
    const stack = [];
    let result = "YES";

    for (let j = 0; j < string.length; j++) {
      if (string[j] === "(") stack.push(string[j]);
      else {
        if (!stack.pop()) {
          result = "NO";
          break;
        }
      }
    }
    if (stack.length) result = "NO";
    console.log(result);
  }
}
