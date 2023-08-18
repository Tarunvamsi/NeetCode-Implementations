/*People in Cubeland use cubic coins. Not only the unit of currency is called a cube but also the coins are shaped like cubes and their values are cubes.
Coins with values of all cubic numbers up to 9261(=21^3), i.e., coins with the denominations of 1, 8, 27,...., up to 9261 cubes, are available in Cubeland.
Your task is to count the number of ways to pay a given amount using cubic coins of Cubeland. 
For example, there are 3 ways to pay 21 cubes: twenty-one 1 cube coins, or one 8 cube coin and thirteen 1 cube coins, or two 8 cube coin and five 1 cube coins.

Input Format:

Input containing a single an integer amount to be paid. You may assume that all the amounts are positive and less than 10000.

Output Format:

Output containing a single integer representing the number of ways to pay the given amount using the coins available in Cubeland.

Note: Refer Sample Input and Sample Output for formatting specifications.

Sample Input 1:

10

Sample Output 1:

2

Explanation:

There are 2 ways to pay 10 cubes: ten 1 cube coins [ 10*1=10], or one 1 cube coin and one 9 cube coin [ (11) + (19) = 10].*/


#include <bits/stdc++.h>
using namespace std;
#define ull unsigned long long
#define ms(a,b) memset(a, b, sizeof a)
#define pb push_back

ull dp[10100];
ull coins[30];

int main(){
	for(ull i = 1 ; i < 22 ; i++){
		coins[i] = (i*i*i);
	}
	//for(ull i = 1 ;i < 22 ;i++)cout<< coins[i] << " ";
	dp[0] = 1;
	for(ull i = 1; i < 22; i++){
		for(ull j = coins[i] ; j < 10100; j++){
      if(dp[j - coins[i]]){
        dp[j] += dp[j - coins[i]];
      }
		}
	}

	ull n;

	while(cin >> n){
    cout<< dp[n] << endl;
	}
	return 0;
}



