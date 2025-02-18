class blob
{
private:
    int health;
    int power;
    char color;
    int xCoord;
    int yCoord;
    int num;
public:
    blob();
    blob(int,char);

    int GetX() const;
    void SetX(int);
    
    int GetY() const;
    void SetY(int);
    
    char GetTeam() const;
    void SetTeam(char);
    
    int GetHP() const;
    void SetHP(int);
    
    int GetPwr() const;
    void SetPwr(int);
    
    void Move();
    void Attack();
    bool AttackCheck();
    void DeathCheck();
};