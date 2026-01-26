#include <defcnAPP.h>
SECTION Application //********** Sezione Applicativo **************************

// inserire qui la dichiarazione dei dati dell'applicativo

typedef struct {
    dword ofX;                  // Origine X del campo
    dword ofY;                  // Origine Y del campo
    dword ofZ;                  // Origine Z del campo
    dword ofU;                  // Origine U del campo (non ancora gestito)
    dword ofV;                  // Origine V del campo (non ancora gestito)
    dword ofW;                  // Origine W del campo (non ancora gestito)
} ORIGINI;

// Allocazione mappa generale della memoria.

// inserire qui l'allocazione dei dati dell'applicativo

typedef struct {
    string msg[NUM_MSG_LEN];
} TBLSTR;

TBLSTR     strtab[NUM_STR_TAB];         // String TABLE di 128 messaggi da 64 char
RETAIN TBLSTR     Rstrtab[NUM_STR_TAB_RTN]; // String TABLE di 128 messaggi da 64 char TAMPONATA

byte  V[NUM_APP_V];                 // Registri PLC non tamponati
byte  W[NUM_APP_W];                   // Registri da PLC a PC
byte  RR[NUM_APP_RR];                 // Registri da PC a PLC
byte  CC[NUM_APP_CC];                 // Registri da PC a PLC
RETAIN byte  MM[NUM_APP_MM];          // Registri del PLC tamponati
dword EDK[NUM_APP_EDK];               // Registri da CN a PLC (E10000)
dword EVK[NUM_APP_EVK];               // Registri da CN a PLC (E20000)
dword ETK[NUM_APP_ETK];               // Registri da CN a PLC (E30000)
dword EQK[NUM_APP_EQK];               // Registri da CN a PLC (E40000)
RETAIN dword EOK[NUM_APP_EOK];        // Registri da CN a PLC (E80000)

double EAK[NUM_APP_EAK];                // Registri a doppia precisione
RETAIN double EBK[NUM_APP_EBK];         // Registri a doppia precisione TAMPONATI

//-------------------- Registri di servizio per ogni canale ---------------
RETAIN dword   numpp[NUM_CANALI];       // numero PP da GUI per PLC da girare su C_NUMPPGM
dword   stato[NUM_CANALI];              // Stato comandato da GUI per il PLC
ORIGINI Or[NUM_CANALI];                 // Origini pezzo per ogni canale

//-------------------------------------------------------------------------
word            FEED;

RETAIN dword    PlcOp[NUM_PLCOP];      // Opzioni del PLC
RETAIN dword    CostK[NUM_COSTK];      // Costanti K

ENDSECTION Application //*************** Sezione Applicativo ******************


#include <defcn.USR> // File defcn per dati utente
