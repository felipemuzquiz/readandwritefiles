def main():
    outfile = open('clients.txt', 'r')

    count = 1

    for client in outfile:
        print(f'{count}. {client.rstrip('\n')}')
        count +=1

    outfile.close()

if __name__ == '__main__':
    main()