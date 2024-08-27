print(
    *(lambda data: [data[idx:]+data[:idx] for idx in range(len(data))])(input()),
    sep='\n'
)