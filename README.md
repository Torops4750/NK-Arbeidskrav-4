# NK-Arbeidskrav-4

Her har eg eit python-script som sett opp SSH på cisco-einingar, og nokre ansible-script, som sett opp.

## Python
For å bruke python-scriptet treng ein python3 og pyserial, samt ein seriellkopling til eininga.
Man startar ved å opne filplasseringa i ein terminal, og så køyre scriptet med "py ssh.py"
Scriptet vil be om ein rekke variablar, t.d. kva OS som scriptet blir køyrt frå, som den treng for å konfigurere alt, merk at viss du skriv inn noko feil, må du avbryte og starte på nytt.

## Ansible
For å køyre ansible-playbooks, må du bruke linux, med ansible og paramiko installert. Du må ha ein ansible conf fil, og ein host fil, med alle cisco-einingane, inkludert IP
Ingen aav playbooks har variablar, grunna tidsmangel, men eg skulle gjerne ha fått det med. 

Ein må fyrst kople til ssh-portane op switchane, og køyre alle switch-playbooks
På switch3 skal ein også køyre etherchannel-playbook
Via switch1 kan ein køyre router.yaml og DHCP.yaml

Switch-playbooks setter opp vlan og trunks på switchane, etherchannel.yamml setter opp etherchannel på switch 3, router.yaml sett opp begge routarane, med HSRP og subinterface, og DHCP.yaml sett opp dhcp-server på begge ruterane, med forskjellige exclusions
