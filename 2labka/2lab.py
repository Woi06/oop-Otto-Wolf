
    san1 = float(input("Бірінші can: "))
    san2 = float(input("Екінші can: "))

    # 1. Қосу
    qosindisi = san1 + san2
    print(f"Қосу: {san1} + {san2} = {qosindisi}")

    # 2. Алу (азайту)
    aiyrmasi = san1 - san2
    print(f"Алу: {san1} - {san2} = {aiyrmasi}")

    # 3. Көбейту
    kobeitindisi = san1 * san2
    print(f"Көбейту: {san1} * {san2} = {kobeitindisi}")

    # 4. Бөлу
    if san2 != 0:
        bolindisi = san1 / san2
        print(f"Бөлу: {san1} / {san2} = {bolindisi}")

        # 5. Бүтін бөлу
        butin_bolindisi = san1 // san2
        print(f"Бүтін бөлу: {san1} // {san2} = {butin_bolindisi}")

        # 6. Бөлу қалдығы
        if san2 != 0:
            kaldyk = san1 % san2
            print(f"Бөлу қалдығы: {san1} % {san2} = {kaldyk}")
        else:
            print("Қате: Нөлге бөлу мүмкін емес.")

    # 7. Дәрежеге шығару
    darezhe = san1 ** san2
    print(f"Дәрежеге шығару: {san1} ** {san2} = {darezhe}")
