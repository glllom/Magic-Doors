#define         NUM_CANALI             25   // Parametri e registri canali.
#define         NUM_ASSI              144   // Parametri e registri assi.
#define         NUM_CZONE               6   // Struttura Correzione Zone.
#define         NUM_MAG                 6   // Struttura Magazzino Tools ( Revolver )
#define         NUM_WEAR                5   // Struttura Usura e Vita Utensile.
#define         NUM_NC                 10   // Correttori Utensili tipo system 1
#define         NUM_TWI                10
#define         NUM_THD                10
#define         NUM_CED                10
#define         NUM_TAB                 1
#define         NUM_GORG                1
#define         NUM_PROBE               4   // Numero Probe
#define         NUM_TORCIA              4   // Numero Torce Taglio Plasma
#define         NUM_GANTRY              2   // Numero Assi Gantry
#define         NUM_VRTC                6   // Tabelle compensazione vettoriale run-time
#define         NUM_VRTC_TRANS_PTS     32
#define         NUM_VRTC_TRANS_SEN      4
#define         NUM_VRTC_TRANS_KP       4
#define         NUM_LNDC_TRANS          4
#define         NUM_LNDC_TRANS_PTS     32

#define         NUM_VG                128   // Variabili globali ISO
#define         NUM_VL                 32   // Variabili locali ISO
#define         NUM_NEST                8   // Numero di nesting ISO
#define         NUM_VA                 32   // Variabili automatiche ISO

#define         NUM_C                 128   // Registri C
#define         NUM_M                 256   // Registri M del PLC
#define         NUM_R                 128   // Registri R del PLC

#define         NUM_COUNTER            30   // Counter del PLC
#define         NUM_PLCERR              8   // Bit Array per allarmi PLC
#define         NUM_PLCMSG              8   // Bit Array per messaggi PLC

#define         NUM_EVPLC               1   // 4001   // Buffer log eventi PLC
#define         NUM_AXQTE               1   // 4001   // Buffer log quote assi da PLC
#define         NUM_MT                 20   // Registri log PLC a bit
#define         NUM_RT                 20   // Registri log PLC a dword

#define         DE_NUM_DRV              1   // Numero driver per RING D.Electron
#define         DE_NUM_RINGS            1   // Numero rings D.Electron
#define         NUM_RINGS               1   // Numero rings Sercos / Mechatrolink
#define         NUM_DRV                16   // Numero drives per ring
#define         NUM_CAN_RINGS           2   // Numero ring CanOpen
#define         NUM_CAN_NODES         128   // Numero nodi CanOpen
#define         NUM_OBJ                32   // Numero oggetti per nodo

#define         SYNC_MARKERS           32   // Sincronizzazione multicanale

#define         NUM_IOX                32   // Numero inp. o outp. per redirezione
#define         NUM_IOXDW               1   // Deve essere (NUM_IOX / 32)

