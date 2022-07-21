package dao;

import javabeans.Reserva;
import java.util.List;
import javax.persistence.Query;

public class ReservaDAO extends DataAccessObject {

    public ReservaDAO() {
        super(Reserva.class);
    }

    @Override
    public List listar() {
        String jpql = "select R from Reserva R";
        Query query = this.manager.createQuery(jpql);
        
        return query.getResultList();
    }
    
}
