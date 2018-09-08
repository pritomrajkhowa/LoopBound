int counter(int N)
{
int ticks=0;
__VERIFIER_assume(N>0);

for(int a=0;a<N;a++)
    for(int b=0;b<N;b++)
        for(int c=0;c<N;c++)
            ticks++;

}