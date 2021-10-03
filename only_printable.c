#include <stdio.h>
#include<string.h>

int main(void) {
	char inp[23]="lrgm{YFnRsdZo;{=jyAbB}";
	int local_1c = 5;
	int sVar1;
	int local_20 = 0;
	while (local_20 < 4) {
		inp[local_20] = inp[local_20] + -6;
		local_20 = local_20 + 1;
	}
	for(;;) {
	sVar1 = strlen(inp);
		if (sVar1 - 1 <= (long)local_1c) break;
		inp[local_1c] = (inp[local_1c] - (char)local_1c) + '\x05';
		local_1c = local_1c + 1;
	}
	printf("Flag: %s",inp);
	return 0;
}

