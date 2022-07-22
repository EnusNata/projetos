package DAO;

import java.util.List;
import javabeans.Cliente;
import javax.persistence.Query;

/**
 *
 * @author Enus
 */
public class ClienteDAO extends DataAccessObject{

    public ClienteDAO() {
        super(Cliente.class);
    }

    @Override
    public List listar(Object obj) {
        String jpql = "select C from Cliente C";
        Query query = this.manager.createQuery(jpql);
        
        return query.getResultList();
    }
}
