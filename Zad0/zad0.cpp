#include <stdio.h>
#include <json/value.h>
#include <fstream>

using namespace std;

vector <char> alphabet;
vector <string> states;
string initial;
unordered_set <string> accepting;
map <pair <string, char>, string> transitions;

int main(){
    //WCZYTAJ JSON!
    string current = initial;
    char c = getchar();
    while(c!= EOF){
        if(c=='\n'){
            if(accepting.find(current)!=accepting.end())
                printf("yes\n");
            else
                printf("no\n");
            current = initial;
            continue;
        }
        current = transitions[make_pair(current, c)];
        c = getchar();
    }
}
