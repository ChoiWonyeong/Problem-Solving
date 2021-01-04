#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;
priority_queue<int, vector<int>, less<int>> maxpq; // 내림차순
priority_queue<int, vector<int>, greater<int>> minpq; // 오름차순
vector<int> answer;
int main() {
	int n;
	int a;
	int maxvalue = 0;
	cin >> n;
	cin >> a;
	maxpq.push(a);
	answer.push_back(a);
	for (int i = 0; i < n-1; i++) {
		cin >> a;
		if (i % 2 == 0) {
			if (a < maxpq.top()) {
				minpq.push(maxpq.top());
				maxpq.pop();
				maxpq.push(a);
				answer.push_back(maxpq.top());
				continue;
			}
			minpq.push(a);
		}
		else {
			if (a > minpq.top()) {
				maxpq.push(minpq.top());
				minpq.pop();
				minpq.push(a);
				answer.push_back(maxpq.top());
				continue;
			}
			maxpq.push(a);
		}
		answer.push_back(maxpq.top());
	}
	//printf("======================================================\n");
	//while (!maxpq.empty()) {
	//	printf("%d ", maxpq.top());
	//	maxpq.pop();
	//}
	//printf("\n");
	//while (!minpq.empty()) {
	//	printf("%d ", minpq.top());
	//	minpq.pop();
	//}
	//printf("\n");
	//printf("======================================================\n");
	for (int i = 0; i < answer.size();i++) {
		printf("%d\n", answer[i]);
	}
	return 0;
}