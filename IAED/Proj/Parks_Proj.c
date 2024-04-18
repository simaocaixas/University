/* iaed24 - ist1109632 - projetc */
#include <stdio.h>
#include <stdlib.h>  
#include <string.h>
#include <ctype.h>

#include "Aux_1.h"
#include "Aux_2.h"
/*

Five constants to define: 
    maximum date string lenght introduced, eg: "01-01-2001 09:20";   
    maximum registration string lenght introduced, eg: "AA-00-AA";  
    maximum parks introduced in the system;
    maximum buff size;
    the maximum number of nodes for one park;

*/

#define DATE 20                                                                 
#define REGI 20  
#define MAXPARKS 20
#define INITBUFFER 10000
#define MAXCARS 20000

#define LETTER 2                                                                // tree constants used in verify_regi function as states 
#define NUM 1
#define NOTHING 0

typedef struct {
    /*
    Struct that contains a list of information from one park. Each park has one list of 5 value floats;
    [Max Lotation, Value paid first 4 15 M, Value paid for 15 M after 1 H, Value per Day, Current Lotation]
    M = minutes;  
    H = hours;
    */

    float info[5]; 
    
} ParkInfo;

typedef struct Node {     
    /*
    Struct that contains the node that follows the hashtables, each node has four components such that they are 
    easily accessible and deleted if needed.
    Registration ->  Entry Date -> Exit Date -> Value Paid
    AA-00-AA -> 01-01-2024 09:03 -> 02-01-2024 09:03 -> 12.20
    */

    char entryregi[REGI];
    char entrydate[DATE]; 
    char exitdate[DATE]; 
    float value_paid; 
    struct Node *next;

} Node;

typedef struct {
    /*
    Struct that contains the componets to easly acess each part of the date format.
    01-01-2024 09:20 day = 1 month = 1 year = 2024 hour = 9 minute = 20.
    */

    int day;
    int month;
    int year;
    int hour;
    int minute;

} Time;

typedef struct {

    Node *table[MAXCARS];  

} HashTable;

typedef struct {

    HashTable *park_table[MAXPARKS]; 

} ParkHash;

typedef struct {
    /*
    Struct that contains registrations and only the this format of a date DD:MM:HM used 
    in the command f with two arguments.
    */

    char plate[REGI];
    char date[DATE];
    float value_paid;

} CarInfo;

unsigned int hash(const char *registration) {   
    /*
    Function hash recives a pointer to a string, and returns the index to the 
    hashtable. The string recived is always a registration, eg: "AA-00-AA".
    */

    unsigned int hash = 0;
    int len = strlen(registration);

    for (int i = 0; i < len; i++) {
        hash = 31 * hash + registration[i];                                     // 31 is a common prime number used in hashing to avoid colisions
    }
    
    return hash % MAXCARS;                                                      
}

void initialize_hash_table(HashTable *table) {
    /*
    Function initialize_hash_table is a void function that recives a pointer to
    a stuct, this struct is always an empty hashtable.
    */

    for (int i = 0; i < MAXCARS; i++) {
        table->table[i] = NULL;
    }
}

int check_park_index(char *names[], char parkName[], int pkCT) {
    /*
    Function check_park_index recives a integer that indicates the current 
    parkcounter, one array that indicates one park name and one pointer to
    an array of pointers that are all the current park names. Returns -1 if the 
    park name is not in names[], else returns his index.
    
    */

    for (int i = 0; i < pkCT; i++) {
        if (strcmp(parkName, names[i]) == 0) {
            return i;
        }
    }
    return -1;
}

int check_park(char *names[], char parkName[]) {
    /*
    Function check_park recives a integer that indicates the current 
    parkcounter and one pointer to an array of pointers that are all the current park names.
    Returns 0 if the park name is not in names[], else returns 1. 
    
    */

    int i = 0;
    while (names[i] != NULL) {
        if (strcmp(parkName, names[i]) == 0) {
            return 0; 
        }
        i++;
    }
    return 1; 
}

void printparks_r(char *names[], int pkCT) {
    /*
    Function printparks_r recives a integer that indicates the current 
    parkcounter and one pointer to an array of pointers that are all the current park names.
    Prints every name in names[].

    */

    for (int i = 0; i < pkCT; i++) {
        if (names[i] != NULL) {
            printf("%s", names[i]);
            putchar('\n');
        }
    }
}

void printparks(char *names[], ParkInfo pkinfo[], int pkCT) {
    /*
    Function printparks recives a integer that indicates the current 
    parkcounter, one pointer to an array of pointers that are all the current park names
    and one struct that contains the park info of the park of index pkCT.

    */

    for (int i = 0; i < pkCT; i++) {
        if (names[i] != NULL) {
            printf("%s ", names[i]);
            printf("%d %d", (int)pkinfo[i].info[0], (int)pkinfo[i].info[4]);
            printf("\n");
        }
    }
}

int insert_into_hash_table(Node *table[], unsigned int hindex, Node *newNode) {
    /*
    Function insert_into_hash_table recives a unsigned integer (only > 0) that indicates the current 
    index of the hashtable and two pointers to the struct Node. Always returns 1.

    */

    if (table[hindex] == NULL) {
        table[hindex] = newNode;
        return 1;                                                               // Insertion successful
    } else {
        Node *current = table[hindex];                                           
        while (current->next != NULL) {                                         // Searches the next possible place to isert node
            current = current->next;
        }
        current->next = newNode;
        return 1;                                                              
    }
}

int is_already_there(char regi[], ParkHash *parkHash) {
    /*
    Function is_already_there recives the array that contains the registration and
    a pointer to ParkHash struct that points to all of the park hashtables. Returns 
    1 if the registration is already in one of the hashtables, else return 0.

    */

    unsigned int hash_index = hash(regi);   

    for (int park_index = 0; park_index < MAXPARKS; park_index++) {                                                     // catches the park hashtables one by one starting at index 0 and going ultil reaches const MAXPARKS
        if (parkHash->park_table[park_index] != NULL) {
            Node **table = parkHash->park_table[park_index]->table;                                                     // double pointer to the current park hashtable
            if (table[hash_index] != NULL) {
                Node *current = table[hash_index];                                                                      
                while (current != NULL) {
                    if (strcmp(current->entryregi, regi) == 0 && strcmp(current->exitdate, "") == 0) {
                        return 1;  
                    }   
                    current = current->next;                                                                            // the information for each car is displaced in a linked list so it easy to run over all the cars 
                }
            }
        }
    }
    return 0;
}


float valuetopay(int minutesdifference, ParkInfo pkinfo[], int I) {
    /*
    Function valuetopay recives the array that contains the information needed to 
    calculate the valued paid for one particular car that was there (minutesdifference)
    minutes, the integer I represents the index of the park.
    Returns a float that is the value to be paid.

    */

    float X = pkinfo[I].info[1], Y = pkinfo[I].info[2], Z = pkinfo[I].info[3]; 
    float val = 0; 
    int Hours = minutesdifference /60, remainingMinutes = minutesdifference %60; 
    int quarters = 0;                                                                                                   // it helps to calculate the value paid breaking down the hours in 15 minutes quartes 

    if (Hours < 1) {
        quarters = (remainingMinutes + 14) / 15;                                                                        // remainingMinutes + 14 so that if it is lower than 15 minutes it still counts as a quarter 
        val = quarters * X; 

    } else if (Hours < 24 && Hours > 0) {
        val += X * 4; 
        val += ((Hours - 1) * (Y * 4)); 
        quarters = (remainingMinutes + 14) / 15; 
        val += quarters * Y; 

        if (val > Z) {                                                                                                  // Z is as well the maximum value paid for a single day
            return Z;
        }

    }  else if (Hours >= 24) {      

        float val_to_sum = 0;
        int days = Hours / 24;

        val = val + (days * Z);    
        Hours %= 24;

        if (Hours > 0) {
            val_to_sum += (4 * X);
            val_to_sum += ((Hours - 1) * (Y * 4)); 
            quarters = (remainingMinutes + 14) / 15;
            val_to_sum += quarters * Y; 
            if (val_to_sum > Z) {
            val_to_sum = Z; 
            }   
            val += val_to_sum;
            return val;
        }   

        else if (remainingMinutes > 0) {
        quarters = (remainingMinutes + 14) / 15; 
        if (quarters <= 4) {
            val_to_sum += (quarters * X);
        } else if (quarters > 4) {
            val_to_sum += (4 * X) + (quarters - 4 * Y); 
        }
        if (val_to_sum > Z) {
        val_to_sum = Z; 
        }          
        val += val_to_sum;
        }
    }
    return val;
}

float find_value_paid_for_date(HashTable *park_table, char *date) {
    /*
    Function find_value_paid_for_date recives a pointer to a array thar is a date
    in the format "DD-MM-AAAA" and a pointer to the struct Hashtable that is an 
    hashtable. Enters the nodes and searches for the valued paid on that particular
    date. Returns that float.

    */

    float total_paid_for_date = 0.0;

    for (int i = 0; i < MAXCARS; i++) {
        Node *current = park_table->table[i];
        while (current != NULL) {
            char working_date[DATE] = "00-00-00";
            sscanf(current->exitdate,"%s %*s", working_date);                   // %*s ignores the "... DD:HM"
            if (strcmp(working_date, date) == 0) {
                total_paid_for_date += current->value_paid;
            }
            current = current->next;
        }
    }

    return total_paid_for_date;
}

void bubbleSortCars(CarInfo cars[], int n) {
    /*
    Function bubbleSortCars recives a pointer to the struct CarInfo that contains
    the unique registrations of a particular park and the date on exit. The integer n represents the 
    number of registrations in cars[]. It orders the registrations as needed (ASCII order).

    */
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (strcmp(cars[j].date, cars[j + 1].date) > 0) {
                CarInfo temp = cars[j];
                cars[j] = cars[j + 1];
                cars[j + 1] = temp;
            }
        }
    }
}

char **cloneStringArray(char *arr[], int n) {
    /*
    Function cloneStringArray recives a double pointer to an array that contains
    park names and an integer that represents the number of parks names, 
    this function runs over the array and makes a deep copy. Uses dinamic memory
    because the parkname is initialy as well allocated with dinamic memory.
    Ŕeturns the deep copy variable called clone.

    */
    char **clone = malloc(n * sizeof(char *));
    if (clone == NULL) {
        return NULL;
    }
    for (int i = 0; i < n; i++) {
        clone[i] = malloc((strlen(arr[i]) + 1) * sizeof(char));
        if (clone[i] == NULL) {

            for (int j = 0; j < i; j++) {
                free(clone[j]);
            }
            free(clone);
            return NULL;
        }
        strcpy(clone[i], arr[i]);
    }
    return clone;
}


float search_regi_u(char *names[], char oldregis[], ParkHash *parkHash) {

    unsigned int hash_index = hash(oldregis);
    char *names_to_order[MAXPARKS];                                                                                     
    int i = 0;            
    float total_val = 0;                                                                                  
    while (names[i] != NULL) {
        names_to_order[i] = names[i];
        i++;
    }
    names_to_order[i] = NULL;
    bubbleSort(names_to_order, i);                              

    for (int j = 0; names_to_order[j] != NULL; j++) {
        int park_index = check_park_index(names, names_to_order[j], MAXPARKS);
        if (park_index >= 0) {
            if (parkHash->park_table[park_index] != NULL) {
                Node **table = parkHash->park_table[park_index]->table;                                                 
                if (table[hash_index] != NULL) {
                    Node *current = table[hash_index];                                                                  
                    while (current != NULL) {                                                                           
                        if (strcmp(current->entryregi, oldregis) == 0) {                                                    
                            if (strcmp(current->exitdate, "") != 0) {
                                total_val = total_val + current->value_paid;
                            } 
                        }
                        current = current->next;
                    }
                }
            }
        }
    }
    return total_val;
}

int func_u(char *names[], char *input, ParkHash *parkHash) {
    char oldregis[REGI];          
    float total = 0;

    if (sscanf(input,"%*s %s", oldregis) != 1) {
        return 0;
    } else if (verify_regi(oldregis) == 0) {
        printf("%s: invalid licence plate.\n", oldregis);
        return 0;
    } 
    total = search_regi_u(names, oldregis, parkHash);
    printf("%0.2f\n", total);
    return 1;
}


int func_r(char *names[], char *input, ParkHash *parkHash, int pkCT, ParkInfo *pkinfo) {

    char *pkname = catch_name(input, 'r');
    int i, pk_index = check_park_index(names, pkname, pkCT);

    if (pk_index == -1) {                                                       // needed to make sure we are not adressing a park that doesnt exists
        printf("%s: no such parking.\n", pkname);
        free(pkname);
        return pkCT;
    }

    for (int i = 0; i < MAXCARS; i++) {                                         // during this loop it frees the nodes from the hashtable 
        Node *current = parkHash->park_table[pk_index]->table[i];
        while (current != NULL) {
            Node *temp = current;
            current = current->next;
            free(temp);
        } 
    }
    free(parkHash->park_table[pk_index]); free(names[pk_index]);
    names[pk_index] = "NOTHING_TO_SEE";

    for (i = pk_index; i < pkCT - 1; i++) {                                     // updates everything that was in 'front' the park deleted 
        names[i] = names[i + 1];
        parkHash->park_table[i] = parkHash->park_table[i + 1];
        pkinfo[i].info[0] = pkinfo[i + 1].info[0];
        pkinfo[i].info[1] = pkinfo[i + 1].info[1];
        pkinfo[i].info[2] = pkinfo[i + 1].info[2];
        pkinfo[i].info[3] = pkinfo[i + 1].info[3];
        pkinfo[i].info[4] = pkinfo[i + 1].info[4];
    }

    char **names_copy = cloneStringArray(names, pkCT);

    names[pkCT-1] = NULL;
    parkHash->park_table[pkCT - 1] = NULL;
    pkCT--;
    
    free(pkname);
    bubbleSort(names_copy, pkCT);                                               // it orders the remains parknames to print 
    printparks_r(names_copy, pkCT);

    for (i = 0; i < pkCT + 1; i++) {
        free(names_copy[i]);
    }

    free(names_copy);
    return pkCT;
}

int process_input_with_two_arg(char *names[], char *pkname, char *datesearch, ParkHash *parkHash, int pkCT) {

    int pk_index = check_park_index(names, pkname, pkCT);
    HashTable *park_table = parkHash->park_table[pk_index];                     // hashtable that will be run over
    Node *current;

    CarInfo cars[MAXCARS];                                                      // cars is the array that will contain and then be order the dates and registrations 
    int car_count = 0;

    for (int i = 0; i < MAXCARS; i++) {
        current = park_table->table[i];
        while (current != NULL) {
            char date[DATE];
            if (sscanf(current->exitdate, "%s %*s", date) == 1) {               // this sscanf is needed to compare only the "DD-MM-AAAA" part
                if (strcmp(date, datesearch) == 0) {
                    strcpy(cars[car_count].plate, current->entryregi);
                    char hm[DATE];
                    sscanf(current->exitdate,"%*s %s", hm);                     // this sscanf is needed to change the date to "HH:MM"
                    strcpy(cars[car_count].date, hm);
                    cars[car_count].value_paid = current->value_paid;
                    car_count++;
                }
            } 
            current = current->next;
        }
    }

    bubbleSortCars(cars, car_count);
    for (int i = 0; i < car_count; i++) {
        printf("%s %s %0.2f\n", cars[i].plate, cars[i].date, cars[i].value_paid);
    }
    free(pkname);
    return 1;
}

int process_input_with_one_arg(char *names[], char *pkname, ParkHash *parkHash, int pkCT) {
    int counter = 0, pk_index = check_park_index(names, pkname, pkCT);                                                  // counter needed to pass to bubble sort so that the dates are printed in order    
    char dates_to_order[MAXCARS][DATE];                                                                                 // two dimensional array to keep all the dates from all the possible parks 
    HashTable *park_table = parkHash->park_table[pk_index];                                                             

    for (int i = 0; i < MAXCARS; i++) {
        Node *current = park_table->table[i];
        while (current != NULL) {
            if (strcmp(current->exitdate, "") != 0) {
                char date[DATE];
                if (sscanf(current->exitdate, "%s %*s", date) != 1) {
                    return 0;
                }
                int found = 0;
                for (int j = 0; j < counter; j++) {
                    if (strcmp(dates_to_order[j], date) == 0) {
                        found = 1;                                                                                      // variable found works to make sure the same date dont enter the array twice
                    }
                }
                if (!found) {
                    strcpy(dates_to_order[counter], date);                                                               
                    counter++;                                                                  
                }
            }
            current = current->next;
        }
    }

    bubbleSortDates(dates_to_order, counter);
    free(pkname);
    for (int i = 0; i < counter; i++) {
        if (strcmp(dates_to_order[i], "") != 0) {                                                                       // the string compare here is to make sure we dont print dates that dont have 'value'
            float value_paid = find_value_paid_for_date(park_table, dates_to_order[i]);
            printf("%s %.2f\n", dates_to_order[i], value_paid);
        }
    }
    return 1;
}

int get_f_error2(char *names[], char *pkname, int pkCT, char *globalclock, char *datasearch) {
    int Error = 0;
    int index = check_park_index(names,pkname,pkCT);
    char copydate[DATE];
    strcpy(copydate, datasearch);                                               // to make sure the original format is keept and to change to HH:MM the date used in comparations is the copydate 
    strcat(copydate, " 00:00");
    if (index == -1) { 
            printf("%s: no such parking.\n", pkname);
            Error = 1;
    } else if (check_date(copydate) == 1) {
            printf("invalid date.\n");
            Error = 1;
    } else if (mindsdiff(copydate, globalclock) > 0) {                          // in oposition to commands like e, s, here we need to make sure the copydate is 'earlier' then the globalclock
            printf("invalid date.\n");
            Error = 1;
    }
    return Error;
}

int get_f_error(char *names[], char *pkname, int pkCT) {
    int Error = 0;
    int index = check_park_index(names,pkname,pkCT);
    if (index == -1) { 
            printf("%s: no such parking.\n", pkname);
            Error = 1;
    }
    return Error;
}

int func_f(char *names[], char *input, ParkHash *parkHash, int pkCT, char *globalclock) {
    char *pkname = catch_name(input, 'f');
    char datasearch[DATE] = "00-00-00";                                                                              // initialize the variable that will store the date recived as "00-00-00"
    int arg_count = 0;                                                                                                  // used to make sure we do the right f command depending of the number of arguments

    if (input[2] == '"') {
        arg_count = sscanf(input, "%*s \"%[^\"]\" %s", pkname, datasearch);
    } else {
        arg_count = sscanf(input, "%*s %s %s", pkname, datasearch);
    }
    if (arg_count == 1) {
        if (get_f_error(names,pkname,pkCT) != 0) {
        free(pkname);
        return 0;
        }
        int result = process_input_with_one_arg(names, pkname, parkHash, pkCT);                                         // if the input only has f park_name
        return result;
    }
    if (arg_count == 2) {
        if (get_f_error2(names,pkname,pkCT, globalclock, datasearch) != 0) {                                            // if the input has f park_name date 
        free(pkname);
        return 0;
        }
        int result = process_input_with_two_arg(names, pkname, datasearch, parkHash, pkCT);
        return result;
    }
    return 0;
}

int search_regi(char *names[], char oldregis[], ParkHash *parkHash) {

    unsigned int hash_index = hash(oldregis);
    char *names_to_order[MAXPARKS];                                                                                     // this array is necessary because they need to be ordered (ASCII order)  
    int found = 0, i = 0;                                                                                               // this funtion returns found such that func_v cant print erro if
    while (names[i] != NULL) {
        names_to_order[i] = names[i];
        i++;
    }
    names_to_order[i] = NULL;
    bubbleSort(names_to_order, i);                              

    for (int j = 0; names_to_order[j] != NULL; j++) {
        int park_index = check_park_index(names, names_to_order[j], MAXPARKS);
        if (park_index >= 0) {
            if (parkHash->park_table[park_index] != NULL) {
                Node **table = parkHash->park_table[park_index]->table;                                                 // hashtable corresponding to this park_index
                if (table[hash_index] != NULL) {
                    Node *current = table[hash_index];                                                                  // current node of the hashtable
                    while (current != NULL) {                                                                           
                        if (strcmp(current->entryregi, oldregis) == 0) {                                                    
                            found = 1;
                            if (strcmp(current->exitdate, "") != 0) {
                                printf("%s %s %s\n", names_to_order[j], current->entrydate, current->exitdate);
                            } else {
                                printf("%s %s\n", names_to_order[j], current->entrydate);
                            }
                        }
                        current = current->next;
                    }
                }
            }
        }
    }
    return found;
}

int func_v(char *names[], char *input, ParkHash *parkHash) {
    char oldregis[REGI];          

    if (sscanf(input,"%*s %s", oldregis) != 1) {
        return 0;
    } else if (verify_regi(oldregis) == 0) {
        printf("%s: invalid licence plate.\n", oldregis);
        return 0;
    } else if (search_regi(names, oldregis, parkHash) == 0) {                   // searchim will run the linked list of the hashtables until the regi is found
        printf("%s: no entries found in any parking.\n", oldregis);
        return 0;
    }
    return 1;
}

int get_s_errors1(int index, char oldregis[], ParkHash *parkHash, char *parkName) {
    int Error = 0;

    if (index == -1) {
        printf("%s: no such parking.\n", parkName);
        Error = 1;
    } else if (verify_regi(oldregis) == 0) {
        printf("%s: invalid licence plate.\n", oldregis);
        Error = 1;
    } else if (is_already_there(oldregis, parkHash) == 0) {
        printf("%s: invalid vehicle exit.\n", oldregis);
        Error = 1;
    }
    return Error;
}

int get_s_errors2(int mins, char dateout[]) {
    /*
    Function get_s_errors2 recives information about the park related to the s 
    command and check/print errors and returns 0 only if there is no errors, else
    returns 1.

    */
    int Error = 0;

    if (mins < 0) { 
            printf("invalid date.\n");
            Error = 1;
    } else if (check_date(dateout) == 1) {
            printf("invalid date.\n");
            Error = 1;
    }
    return Error;
}

int func_s(char *names[], int pkCT, ParkInfo pkinfo[], char *input, ParkHash *parkHash, char* globalclock) {
    char *parkName = catch_name(input, 's'), oldregis[REGI], dateout[DATE];
    
    if (parse_input_regis(input, dateout, oldregis, parkName) != 1) {
        free(parkName);
        return 0;
    }

    unsigned int h_index = hash(oldregis);                                     
    int index = check_park_index(names, parkName, pkCT);                                                                // the hashtables are in the same index as the parkname so therefore this will be useful                                                      

    if (get_s_errors1(index, oldregis, parkHash, parkName) != 0) {
        free(parkName);
        return 0;
    }       
    Node **table = parkHash->park_table[index]->table;                                                                  // table is a double pointer that points to the hashtable of index 'index'   
    Node *current = table[h_index];                                                                                     // curent is the node of the hashtable that in this function we want to adress

    while (current != NULL && (strcmp(current->entryregi, oldregis) != 0 || strcmp(current->exitdate, "") != 0)) {      // finds the only registration with an empty exitdate that matches the registration introduced 
        if (strcmp(current->entryregi, oldregis) == 0 && strcmp(current->exitdate, "") == 0) {                                         
            strcpy(current->exitdate, dateout);                                                                 
            return 1; 
        } else {
            current = current->next;
        }
    }
    
    int minutesdiference = mindsdiff(dateout, globalclock);                                                                                         
    if (get_s_errors2(minutesdiference, dateout) != 0) {
        free(parkName);
        return 0;
    }   
    minutesdiference = mindsdiff(dateout, current->entrydate);                                                          
    float value = valuetopay(minutesdiference, pkinfo, index);                                                          // valuetopay returns the value that will be printed and will be put in the already existing node                                                     
    strcpy(current->exitdate, dateout); current->value_paid = value;
    pkinfo[index].info[4]++;    
    printf("%s %s %s %0.2f\n", oldregis, current->entrydate, current->exitdate, value);
    strcpy(globalclock, dateout);                                                                                
    free(parkName);
    return 1;
}

Node* createNode(char *entryRegis, char *entryDate) {
    /*
    Function createNode recives a pointer to a char thar represents the new registration
    and another one to the entry date and correctly inserts them into the linked lists.
    Returns the node.

    */

    Node *newNode = malloc(sizeof(Node));                                       // dinamic memory is the best option so that later i can easly 'erase' park information 

    strcpy(newNode->entryregi, entryRegis);
    strcpy(newNode->entrydate, entryDate);
    strcpy(newNode->exitdate, "");                                              // initialize exitdate as ' "" ' so later we can check if the car is in or out of the park
    newNode->value_paid = 0;

    newNode->next = NULL;                                                       // the pointer next points to NULL, to make sure the next node dont initiates with unwanted memory                
    return newNode;
}

void e_act_and_print(ParkInfo pkinfo[], char *names[], int index) {
    /*
    Function e_act_and_print recives information about the park and prints it into 
    the terminal. 
    */

    pkinfo[index].info[4]--;                                                    // the car has all the conditions to join the park, so we decrease the current lotation
    printf("%s %d\n", names[index], (int)pkinfo[index].info[4]);
}

int get_e_error1(ParkInfo *pkinfo, int index, char *names[], char *parkname) {
    /*
    Function get_e_error1 recives information about the park related to the e 
    command and check/print errors and returns 0 only if there is no errors, else
    returns 1.
    */
    int Error = 0;

    if (index < 0) {
        printf("%s: no such parking.\n", parkname);
        Error = 1;
    } else if (pkinfo[index].info[4] == 0) {
        printf("%s: parking is full.\n", names[index]);
        Error = 1;
    }
    return Error;
}

int get_e_error2(char newregi[], int minutes, ParkHash parkHash, char *new_date) {
    /*
    Function get_e_error2 recives information about the park related to the e 
    command and check/print errors and returns 0 only if there is no errors, else
    returns 1.
    */

    int Error = 0;                                                              // just like in other get_errors funtions variable Error will only change if and error apear
    if (verify_regi(newregi) == 0) {
        printf("%s: invalid licence plate.\n", newregi);
        Error = 1;
    } else if (is_already_there(newregi, &parkHash) == 1) {                     // is_already_there runs over the hashtable and returns 1 if finds the registration
        printf("%s: invalid vehicle entry.\n", newregi);
        Error = 1;
    }  else if (minutes < 0) { 
            printf("invalid date.\n");
        Error = 1;
    } else if (check_date(new_date) == 1) {                                    
            printf("invalid date.\n");
        Error = 1;
    }   
    return Error;
}

int func_e(char *names[], ParkInfo pkinfo[], char *input, ParkHash *parkHash, char *globalclock, int pkCT) {
    char *parkName = catch_name(input, 'e'), new_regis[REGI], new_date[DATE];
    int minutes = 0;

    if ((parse_input_regis(input, new_date, new_regis, parkName)) != 1) {
        free(parkName);
        return 0;
    }

    int index = check_park_index(names, parkName, pkCT);  
    unsigned int hindex = hash(new_regis);                                      // hindex will be the hashtable index, hashing explained in hash function
    minutes = mindsdiff(new_date, globalclock);                                 // minutes will be the minute diference (current date - last date), so to be an acctual valid date this diference needs to be > 0
    Node *newNode = createNode(new_regis, new_date);

    if (get_e_error1(pkinfo, index, names, parkName) != 0 || 
    get_e_error2(new_regis, minutes, *parkHash, new_date) != 0) {
        free(newNode);
        free(parkName);
        return 0;
    }

    insert_into_hash_table(parkHash->park_table[index]->table, hindex, newNode);
    e_act_and_print(pkinfo, names, index);
    strcpy(globalclock, new_date);                                              // update the globalclock only if everything is right and the info is in the correct place
    free(parkName);
    return 1;
}


void free_q_memory(char *names[], int pkCT, ParkHash *parkHash) {   
    /*
    Function free_q_memory recives both the memory allocated names and the memory
    allocated nodes and properly frees them. 
    */
               
        for (int i = 0; i < pkCT; i++) {                                        // iterates all the current parks 
            free(names[i]);                                                     // for each parkname was allocated memory so this free is necessary
            HashTable *parkTable = parkHash->park_table[i];                     
            if (parkTable != NULL) {
                for (int j = 0; j < MAXCARS; j++) {
                    Node *current = parkTable->table[j];                        // easy way to access the hashtable so that i can free each node
                    while (current != NULL) {
                        Node *next = current->next;
                        free(current);
                        current = next;
                    }
                }
                free(parkTable);                                                // free the 'structure' as well
            }
        }
}

int get_p_errors(float af[], char *names[], char parkname[], int pkCT) {
    /*
    Function get_p_errors recives information about the park related to the p 
    command and check/print errors and returns 0 only if there is no errors, else
    returns 1.

    */
    int Error = 0;
    int index = check_park_index(names, parkname, pkCT);                        // check_park_index return -1 if the park is not yet registered                    
    int len = strlen(parkname);
    int i;

    for (i = 0; i < len; i++) {
        if (parkname[i] <= '9' && parkname[i] >= '0') {
            printf("invalid parking name.\n");
            return 1;
    }
    }
    if (index != -1) {          
        printf("%s: parking already exists.\n", parkname);
        Error = 1; 
    } else if (af[0] <= 0) {                                                    
        printf("%.0f: invalid capacity.\n", af[0]);                             
        Error = 1;
    } else if (af[1] <= 0 || af[2] <= 0 || af[3] <= 0) {
        printf("invalid cost.\n");
        Error = 1;
    } else if (af[1] >= af[3] || af[2] < af[1] || af[2] > af[3]) {
        printf("invalid cost.\n");
        Error = 1;
    } else if (pkCT == MAXPARKS) {                                              // MAXPARKS, a constant that currently is set to 20 
        printf("too many parks.\n");
        Error = 1;
    }
    return Error;
}

int get_p_input(char *input, char *parkName, float af[4]) {

    if (input[2] == '"') {
        if (sscanf(input, "%*s \"%[^\"]\" %f %f %f %f", parkName, &af[0], &af[1], &af[2], &af[3]) != 5) {               //  \"%[^\"]\"   used for names such as "CC Colombo", it will scan everything until the second ' " ' is founded
            return 0; 
        }
    } else {
        if (sscanf(input, "%*s %[^ ] %f %f %f %f", parkName, &af[0], &af[1], &af[2], &af[3]) != 5) {                    
            return 0; 
        }
    }
    return 1; 
}

int func_p(char *names[], ParkInfo pkinfo[], int pkCT, char *input, ParkHash *parkHash) {

    char *parkName = catch_name(input, 'p');                                    
    float af[4];                                                                // array that contains [Max Lotation, X, Y, Z, Current Lotation]
    if ((get_p_input(input, parkName, af) != 1)) {  
        free(parkName);
        return 0;
    }
    if (get_p_errors(af, names, parkName, pkCT) != 0) {
        free(parkName);
        return pkCT;
    }

    names[pkCT] = malloc(strlen(parkName) + 1);                                 // park name can get up to +8000 caracters so dinamic memory is the best option

    strcpy(names[pkCT], parkName);                                              // this array will contain the park names
    free(parkName);

    pkinfo[pkCT].info[4] = af[0];                                               // Initialy max lotation is the same as current lotation
    parkHash->park_table[pkCT] = malloc(sizeof(HashTable));

    initialize_hash_table(parkHash->park_table[pkCT]);
    for (int i = 0; i < 4; i++) {
    pkinfo[pkCT].info[i] = af[i];
    }
    pkCT++;
    return pkCT;
}

void check_input(char *input, char *names[], ParkInfo pkinfo[], int *pkCT, ParkHash *parkHash, char *globalclock) {
    /*
    Function check_input recives six pointers, the park names, the struct parkinfo
    the integer park counter, the struct parkHash that contains all the park hashtables
    and the global clock. This is the major function that redirect the input from
    the terminal to all the commands. 

    */

    if ((strncmp(input, "p", 1) == 0)) {
        if (strlen(input) > 1) {                                                // the command p plays two diferent roles, so this condition is necessary 
            *pkCT = func_p(names, pkinfo, *pkCT, input, parkHash);                 
        } else {
            printparks(names, pkinfo, *pkCT);                                   
        }
    } 
    if (strncmp(input, "e", 1) == 0) {
        func_e(names, pkinfo, input, parkHash, globalclock, *pkCT);
    } else if (strncmp(input, "s", 1) == 0) {
        func_s(names, *pkCT, pkinfo, input, parkHash, globalclock);
    } else if (strncmp(input, "v", 1) == 0) {
        func_v(names, input, parkHash);
    } else if (strncmp(input, "f", 1) == 0) {
        func_f(names, input, parkHash, *pkCT, globalclock);                     
    } else if (strncmp(input, "r", 1) == 0) {
        *pkCT = func_r(names,input,parkHash, *pkCT, pkinfo);                    // park counter increases in func_p and decreases in func_r if they suceed, both return park counter
    } else if (strncmp(input, "u", 1) == 0) {
        func_u(names, input, parkHash);
    }
}

int main() {
    
    char input[INITBUFFER], globalglock[DATE] = {0};                        
    char *names[MAXPARKS + 1] = {0};                                            // array with pointers to each park name

    ParkInfo pkinfo[MAXPARKS] = {0};                                           
    ParkHash parkHash = {0};                                                    // parkHash will be the linekd-list with all the hashtables from each park
    int pkCT = 0;                                                               // park counter, MAXPARKS (max quantity of parks) = 20


    strcpy(globalglock, "00-00-00 00:00");                                      // globalclock will be used to check the last date

    while (1) {
        if (fgets(input, sizeof(input), stdin) == NULL) {
            free_q_memory(names, pkCT, &parkHash);
            return 1;
        }
        long len = strlen(input);
        while (len > 0 && (input[len - 1] == '\n' || input[len - 1] == '\r')) {  
            input[--len] = '\0';
        }
        if (input[0] == 'q') {
            free_q_memory(names, pkCT, &parkHash);                             
            return 0;
        }        
        check_input(input, names, pkinfo, &pkCT, &parkHash, globalglock);
    }
    return 0;
}
