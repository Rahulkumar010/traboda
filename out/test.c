#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void gift(int a,int b)
{
    printf("a: %d\nb: %d\n",a,b);
	if(a==0xfade && b==0xfeed)
	{
		puts("You deserve the Mjolnir!");
		puts("Take it and unleash the power of the god of thunder!");
	}
	else
	{
		puts("Whatcha lookin for kiddo?");
		puts("This is not a toffee shop!");
		exit(0);	
	}
}
int main()
{
	puts("Hey kid!");
	puts("Wanna help Thor get his lost hammer back?");
	puts("Gimme your payload and I shall you your hammer!");
	int a=0,b=0;
	char buf[64];
	gets(buf);
	gift(a,b);
	return 0;
}
