package javabeans;

import javabeans.Pedido;
import javabeans.Produto;
import javax.annotation.Generated;
import javax.persistence.metamodel.SingularAttribute;
import javax.persistence.metamodel.StaticMetamodel;

@Generated(value="EclipseLink-2.7.10.v20211216-rNA", date="2022-07-22T17:32:53")
@StaticMetamodel(PedidoProduto.class)
public class PedidoProduto_ { 

    public static volatile SingularAttribute<PedidoProduto, Produto> produto;
    public static volatile SingularAttribute<PedidoProduto, Pedido> pedido;
    public static volatile SingularAttribute<PedidoProduto, Integer> qtd_produto;
    public static volatile SingularAttribute<PedidoProduto, Long> id;
    public static volatile SingularAttribute<PedidoProduto, Integer> versao;

}