package DAO;

import javabeans.Pedido;
import java.util.List;
import javax.persistence.Query;

/**
 *
 * @author Enus
 */
public class PedidoDAO extends DataAccessObject {

    public PedidoDAO() {
        super(Pedido.class);
    }
    
    @Override
    public List listar(Object obj) {
        String jpql = "select P from Pedido P";
        Query query = this.manager.createQuery(jpql);
        
        return query.getResultList();
    }
    
}
