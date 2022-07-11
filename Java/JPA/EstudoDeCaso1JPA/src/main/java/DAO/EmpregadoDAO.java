package DAO;

import java.util.List;
import javabeans.Empregado;
import javax.persistence.Query;

public class EmpregadoDAO extends DataAcessObject{

    public EmpregadoDAO() {
        super(Empregado.class);
    }

    @Override
    public List listar(Object obj) {
        String jpql = "select E from Empregado E";
        Query query = this.manager.createQuery(jpql);
        return query.getResultList();
    }
    
}
