def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    m_perc = int(input('Enter the number of males:'))
    f_perc = int(input('Enter the number of females:'))
    total = m_perc + f_perc
    

    print (f'The total number of students: \t         {total}')
    print (f'The numbers of males and females: \t {m_perc}      {f_perc} ')
    print (f'The persentage of males and females: \t {m_perc:.2f}%  {f_perc:.2f}% ')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
