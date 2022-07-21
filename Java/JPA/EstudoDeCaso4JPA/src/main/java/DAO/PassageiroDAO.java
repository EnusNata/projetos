package dao;

import javabeans.Passageiro;
import java.util.List;
import javax.persistence.Query;

public class PassageiroDAO extends DataAccessObject {

    public PassageiroDAO() {
        super(Passageiro.class);
    }

    @Override
    public List listar() {
        String jpql = "select P from Passageiro P";
        Query query = this.manager.createQuery(jpql);
        
        return query.getResultList();
    }
    
}
