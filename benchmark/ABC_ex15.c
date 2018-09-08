void ex15(int m, int n, int p, int q) {

        __VERIFIER_assume(m >= 0 && n >=0 && p>=0 && q>=0);
	for (int i = 1; i <= n; i = i + 1)
		for (int j = 1; j <= m; j = j + 1)
			for (int k = i; k <= p; k = k + 1)
				for (int l = q; l <= j; l = l + 1)
					;
}
