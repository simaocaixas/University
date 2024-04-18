// Fist auxiliar file, contains 3 auxiliar functions  

#define LETTER 2
#define NUM 1
#define NOTHING 0
#define INITBUFFER 9000

#include <stdio.h>
#include <string.h>

int verify_regi(char new_regis[]) {  
    /*
    Function verify_regi recives an array that represents a registration and returns
    1 if it is valid, else returns 0;
    
    */
    
    int i, current, len;
    int countLet = 0, countNum = 0;    
    len = strlen(new_regis);
    current = NOTHING;

    if (len != 8) {
        return 0;
    }
    for (i = 0; i < len; i++){
        if (new_regis[i] >= 'A' && new_regis[i] <= 'Z') {
            if (current == NUM) {
                return 0;
            }
            if (current == LETTER) {
                countLet++;
            }
            current = LETTER;
        } else if (new_regis[i] >= '0' && new_regis[i] <= '9') {
            if (current == LETTER) {
                return 0;
            }
            if (current == NUM) {
                countNum++;
            }
            current = NUM;
        }  else if (new_regis[i] == '-') {
            current = NOTHING;
            }
        } 

    if (countNum == 3) {
        return 1;
    }
    
    if (countLet + 1 != countNum && countNum + 1 != countLet) {
        return 0;
    }
    return 1;
}

int check_date(char *date) {
    /*
    Function check_date recives a pointer to an array that represents a date in 
    the format "DD-MM-AAAA" and returns 1 if it is invalid, else returns 0;
    
    */
    int Error = 0;
    int year, month, day, hour, min;
    sscanf(date, "%d-%d-%d %d:%d", &day, &month, &year, &hour, &min);

    if (strstr(date, "-") == NULL || strstr(date, ":") == NULL) {
        Error = 1; 
    } else if (hour < 0 || min < 0 || min >= 60 || hour >= 24 || day > 31) {
        Error = 1;
    } else if (month <= 0 || year <= 0 || day <= 0) {
        Error = 1;
    } else if (month == 2) {
        if (day > 28) {
            Error = 1;
        }
    } else if (month == 4 || month == 6 || month == 9 || month == 11) {
        if (day > 30) {
            Error = 1;
        }
    } else if (month > 12) {
        Error = 1;
    }
return Error;
}

int minpermonth(int Mes) {
    /*
    Function minpermonth recives a integer that indicates a month and returns 
    an integer that is number of minutes from month 0 to that particular month.
    
    */

    int total = 0;

    for (int i = 1; i <= Mes - 1; i++) {
        if (i == 2) { 
            total += 28 * 24 * 60;
        } else if (i == 4 || i == 6 || i == 9 || i == 11) { 
            total += 30 * 24 * 60;
        } else { 
            total += 31 * 24 * 60;
        }
    }

    return total; 
}

int mindsdiff(char *date1, char *current_date) {
    /*
    Function mindsdiff recives two pointers to arrays, these arrays are always 
    dates in the format "DD-MM-AAAA HH:MM" and returns the diference between 
    date1 and current_date, (date1 - current_date), can return negative values.

    */

    int total = 0;
    int year1, month1, day1, hour1, min1, year2, month2, day2, hour2, min2;
    int yearsdiff, daysdiff, hoursdiff, minsdif;

    sscanf(date1, "%d-%d-%d %d:%d", &day1, &month1, &year1, &hour1, &min1);
    sscanf(current_date, "%d-%d-%d %d:%d", &day2, &month2, &year2, &hour2, &min2);

    yearsdiff = year1 - year2;
    daysdiff = day1 - day2;
    hoursdiff = hour1 - hour2;
    minsdif = min1 - min2;

    total = (yearsdiff * 365 * 24 * 60) + (minpermonth(month1) - minpermonth(month2)) +
            (daysdiff * 24 * 60) + (hoursdiff * 60) + minsdif;

    return total;
}


int parse_input_regis(char *I, char *date, char *regi, char *parkname) {
    /*
    Function parse_input_regis recives four pointers to chars, and readress *date,
    *regi and *parkanme bases on the string and I is pointing to.    
    Returns 1 if the parsing was properly done, else returns 0.

    */

    int day, month, year, hour, minute;
    if (I[2] == '"') {
        if (sscanf(I, "%*s \"%[^\"]\" %s %d-%d-%d %d:%d", parkname, regi, &day, &month, &year, &hour, &minute) != 7) {
            return 0;
        }
    } else {
        if (sscanf(I, "%*s %s %s %d-%d-%d %d:%d", parkname, regi, &day, &month, &year, &hour, &minute) != 7) {
            return 0;
        }
    }
    sprintf(date, "%02d-%02d-%04d %02d:%02d", day, month, year, hour, minute);                                          // add the HH:MM format to the DD:MM:AAAA format
    return 1;
}

char* catch_name(char *input, char identifier) {
    /*
    Function catch_name recives one character and a pointer to an array, this 
    function will do things depending on the identifier (ex: 'p' 'e' 's' ..).
    Returns the park name if properly executed else if memory alocation fails 
    returns NULL.
    This fuction uses dinamic memory to adress the posibily of a huge park name.

    */

    char format[20], *name = malloc((INITBUFFER + 1) * sizeof(char)); 
    if (name == NULL) {                                                         // in case of vailing memory alocation
        return NULL;
    }

    if (input[2] == '"') {
        snprintf(format, sizeof(format), "%c \"%%[^\"]\"", identifier);
    } else {
        snprintf(format, sizeof(format), "%c %%s", identifier);
    }

    if (sscanf(input, format, name) == 1) {
        size_t name_len = strlen(name);
        if (identifier == 'r') {
            return name;
        } 

        char *temp = realloc(name, (name_len + 1) * sizeof(char));              
        if (temp == NULL) {                                                     // in case of vailing memory alocation (again)
            free(name); 
            return NULL;
        } else {
            name = temp;
        }
    } else {
        free(name); 
        return NULL;
    }
    return name;
}
