def combination_topup(target, nominal):
    data = [target] + nominal

    if all(x % 1000 == 0 for x in data):
        factor = 1000
    elif all(x % 10 == 0 for x in data):
        factor = 1
    else:
        factor = 1

    target //= factor
    nominal = [n // factor for n in nominal]

    dp = [float("inf")] * (target + 1)
    choice = [-1] * (target + 1)

    dp[0] = 0

    for saldo in range(1, target + 1):
        for topup in nominal:
            if saldo - topup >= 0:
                if dp[saldo - topup] + 1 < dp[saldo]:
                    dp[saldo] = dp[saldo - topup] + 1
                    choice[saldo] = topup

    if dp[target] == float("inf"):
        print("Tidak ada kombinasi tepat")
        return

    kombinasi = []
    saldo = target
    while saldo > 0:
        topup = choice[saldo]
        kombinasi.append(topup * factor)
        saldo -= topup

    print("Jumlah transaksi minimum:", dp[target])
    print("Kombinasi top-up:", kombinasi)

combination_topup(75000, [10000, 20000, 25000, 50000, 100000])