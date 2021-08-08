#include <queue>
#include <cstdio>
using namespace std;
int num = 0;
struct node
{
    int x, y;
    int path;
};
queue <node> qn;
bool chess[10][10];
void set_table()
{
    int i, j;
    for (i = 0; i < 10; i++)
    {
        for (j = 0; j < 10; j++)
            chess[i][j] = false;
    }
}
bool out_of_area(int x, int y)
{
    if (x < 1 || x > 8) return true;
    if (y < 1 || y > 8) return true;
    return false;
}
void input_queue(int x, int y, int n)
{
    struct node temp;
    temp.x = x;
    temp.y = y;
    temp.path = n;
    if (!out_of_area(x, y))
    {
        if (chess[y][x] == false)
        {
            chess[y][x] == true;
            qn.push(temp);
        }
    }
}
int main()
{
    int st, en;
    scanf("%d %d", &st, &en);
    int sx = (st % 8) + 1;
    int sy = (st / 8) + 1;
    int ex = (en % 8) + 1;
    int ey = (en / 8) + 1;

    /*printf("%d %d\n", sx, sy);
    printf("%d %d\n", ex, ey);*/

    set_table();

    input_queue(sx, sy, 0);

    while (!qn.empty())
    {
        auto temp = qn.front(); qn.pop();
        int x = temp.x, y = temp.y, n = temp.path;

        if (x == ex && y == ey)
        {
            num = n;
            break;
        }
        input_queue(x + 1, y - 2, n + 1); // 1
        input_queue(x - 1, y - 2, n + 1); // 2
        input_queue(x + 1, y + 2, n + 1); // 3
        input_queue(x - 1, y + 2, n + 1); // 4
        input_queue(x - 2, y + 1, n + 1); // 5
        input_queue(x - 2, y - 1, n + 1); // 6
        input_queue(x + 2, y + 1, n + 1); // 7
        input_queue(x + 2, y - 1, n + 1); // 8
    }
    printf("%d", num);
}
