#include<bits/stdc++.h>

using namespace std;

vector<int> parent(200005,-1);
vector<int> rank_i(200005,1);
int m;
vector<vector<int>>graph;

int find(int i){
    if(parent[i]==-1)return i;
    else{
        int res=find(parent[i]);
        parent[i]=res;
        return res;

    }
}

void unite(int x,int y){
    int s1=find(x);
    int s2=find(y);
    if(s1!=s2){
        if(rank_i[s1]<rank_i[s2]){
            rank_i[s2]+=rank_i[s1];
            parent[s1]=s2;
        }
        else{
            parent[s2]=s1;
            rank_i[s1]+=rank_i[s2];
        }
    }
}

void kruskal(){
    sort(graph.begin(),graph.end());
    int tot=0,ans=0;
    for(auto edge:graph){
        int a=edge[1];
        int b=edge[2];
        int c=edge[0];
        if(find(a)!=find(b)){
            unite(a,b);
            tot++;
            ans+=c;
            cout<<a<<" -- "<<b<<"  Edge number "<<tot<<"\n";
        }
    }
    cout<<"\nCost is : "<<ans<<"\n";
}

signed main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n;
    cin>>n;
    cin>>m;
    for(int i=0;i<m;i++){
        int a,b,c;
        cin>>a>>b>>c;
        graph.push_back({c,a,b});
    }
    cout<<endl;
    kruskal();
    return 0;
}


// 5 8
// 1 3 75
// 3 4 51
// 2 4 19
// 3 2 95
// 2 5 42
// 5 4 31
// 1 2 9
// 3 5 66

// 5
// 7
// 0 1 2
// 0 3 6
// 2 1 3
// 3 1 8
// 4 1 5
// 4 2 7
// 4 3 9