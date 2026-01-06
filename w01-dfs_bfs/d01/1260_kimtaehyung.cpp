#include<bits/stdc++.h>
using namespace std;
//v는 정점의 개수(최대 1000개)
vector<int> v[1000];
int n,m,a;
//방문배열로 해당 노드를 방문했는지 확인 (dfs)
int visited_dfs[1001];
//방문배열로 해당 노드를 방문했는지 확인 (dfs)
int visited_bfs[1001];

void dfs(int here){
    visited_dfs[here] = 1;
    cout << here << " ";
    for(int b : v[here]){
        if(visited_dfs[b] == 1) continue;
        dfs(b);
    }
    return;
}

void bfs(int here){
    queue<int> q;
    visited_bfs[here] = 1;
    q.push(here);
    while(q.size()){
        int here = q.front();
        cout << here << " ";
        q.pop();
        for(int b : v[here]){
            if(visited_bfs[b]!=0)continue;
            visited_bfs[b]=1;
            q.push(b);
        }
    }

}
int main(){
    //C++ 빠른 입력 위한 메모리 비우기
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    //C++ 입력
    cin >> n >> m >> a;
    for(int i=0; i<m;i++){
        //양방향이기에 각 노드에 푸쉬
        int p,q;
        cin >> p >> q;
        v[p].push_back(q);
        v[q].push_back(p);
    }
    
    dfs(a);
    cout << "\n";
    bfs(a);
    return 0;
}