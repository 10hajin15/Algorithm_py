// 소수 찾기
// https://school.programmers.co.kr/learn/courses/30/lessons/42839

function solution(numbers) {
  let answer = 0;
  const primes = new Set();
  const check = Array.from({length: numbers.length}, () => 0);

  const permutate = (s, L, check) => {
    if(L === numbers.length) {
      s && primes.add(Number(s));
      return;
    } else {
      for(let i = 0; i < numbers.length; i++) {
        if(!check[i]) {
          check[i] = 1;
          permutate(s+numbers[i], L+1, check);
          permutate(s, L+1, check);
          check[i] = 0;
        }
      }
    }
  }
  permutate('', 0, check);

  const isPrime = (n) => {
    if (n <= 1) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if(Number.isInteger(n/i)) return false;
    }
    return true;
  }

  for(let x of primes) {
    isPrime(x) && answer++;
  }

  return answer;
}

console.log(solution("17")); // 3
// console.log(solution("011")); // 2
