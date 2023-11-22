print("Welcome to WordSearch!\n")
print("What difficulty do you want?\n")
diff = input("EASY MEDIUM HARD\n\n")
if diff=='EASY':
    easywordfound = int('0')
    blockone = '''
    C I R C U I T S K Y
    N E T W O R K G H I
    P R O G R A M M I N
    H A R D W A R E P L
    B Y T E A L A P T O
    I N T E R N E T U O
    T E C H N O L O G Y
    M O U S E Y T S Q N
    S O F T W A R E H M'''

    print(blockone)
    print("\nThere are 9 hidden words")
    while easywordfound < 9:
      wordsfound = input("What word did you find?\n")
      if wordsfound in ["CIRCUIT", "NETWORK", "PROGRAM", "HARDWARE", "BYTE", "INTERNET", "TECH", "MOUSE", "SOFTWARE"]:
        easywordfound += 1
        print('You found ' + str(easywordfound) + ' words')
      else:
        print("Sorry that is not a word")
    print('You found all the words!')
    print('Thanks for playing!')
    exit(0)
elif diff=='MEDIUM':
    medwordfound = int('0')
    blocktwo= '''
    S Y S T E M R E S O U R C E S
    I N T E R F A C E O P E R A T I
    A L G O R I T H M I C R E H A C
    S T O R A G E G O O G L E O T S
    M E M O R Y E A H E W O R R Q U
    N E T W O R K R C O D I N G A J
    C O M P I L E R O D T N R O H A
    R E M O T E O P E N S O U R C E Y
    S E C U R I T Y G Y O I H K J W
    A P P L I C A T I O N S C T Z L
    '''
    print(blocktwo)
    print("\nThere are 16 hidden words")
    while medwordfound < 16:
      wordsfound = input("What word did you find?\n")
      if wordsfound in ["SYSTEM", "RESOURCES", "INTERFACE", "OPERATING", "ALGORITHMIC", "RESEARCH", "STORAGE", "GOOGLE", "MEMORY", "NETWORK", "CODING", "COMPILER", "REMOTE", "OPEN SOURCE", "SECURITY", "APPLICATIONS"]:
        medwordfound += 1
        print('You found ' + str(medwordfound) + ' words')
      else:
        print("Sorry that is not a word")
    print('You found all the words!')
    print('Thanks for playing!')
    exit(0)
elif diff=='HARD':
    hardwordfound = int('0')
    blockthree='''
    A S S E M B L E R K H U W A D J A
    D E A D C O D E F S H E L L T Y A
    S U B R O U T I N E X P O I N T R
    H A C K E R B I N A R Y S E O S C
    J U M P L A B Y R I N T H L S A O
    M E T A S T A B I L I T Y A R Y D
    P A R A D I G M C R Y P T O G M G
    R E C U R S I O N Z E R O D A Y S
    F O R T R A N R E G I S T E R V H
    S Y N T A X A N A L Y S I S S S I
    B O O T S T R A P L E G A C Y D K
    O P T I M I Z A T I O N A G O A Y
    S P E C I F I C A T I O N X G I O
    H Y P E R V I S O R S T E G A N O
    G R A P H E N E B L A C K H A T S
    '''
    print(blockthree)
    print("\nThere are 25 hidden words")
    while hardwordfound < 25:
      wordsfound = input("What word did you find?\n")
      if wordsfound in ["ASSEMBLER", "DEADCODE", "SHELL", "SUBROUTINE", "HACKER", "BINARY", "JUMP", "LABYRINTH", "METASTABILITY", "PARADIGM", "CRYPTOGRAPHY", "RECURSION", "ZERO DAYS", "FORTRAN", "REGISTER", "SYNTAX", "ANALYSIS", "BOOTSTRAP", "LEGACY", "OPTIMIZATION", "SPECIFICATION", "HYPERVISOR", "STEGANOGRAPHY", "GRAPHENE", "BLACKHATS"]:
        hardwordfound += 1
        print('You found ' + str(hardwordfound) + ' words')
      else:
        print("Sorry that is not a word")
    print('You found all the words!')
    print('Thanks for playing!')
    exit(0)
else:
    print("Please restart program and enter a valid difficulty.")
    exit(1)